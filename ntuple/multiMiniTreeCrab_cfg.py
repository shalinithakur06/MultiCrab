
#///////////////////////////////////////////////////
#                                                  #
# CRAB configuration to run over Multiple samples  #
#                                                  #
#///////////////////////////////////////////////////


#------------------ Setup CRAB -------------------------------#
#execme("source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh")
#execme("cmsenv")
#execme("voms-proxy-init --voms cms")
#-------------------------------------------------------------#

import os
import sys
import datetime

def execme(cmd):
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd
    os.system(cmd)

import FWCore.ParameterSet.Config as cms

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("ntuple","module"))
from dataMiniAOD import muDataSampDict as muData
from dataMiniAOD import eleDataSampDict as eleData
from mcMiniAOD import mcSampDict as mc
from sampleKeyVal import *
from multiCrab import *

#------------------------------------------
#Check availability of samples on DAS
#------------------------------------------
#toPrint("Total MC samples",len(mc))
for n in range(len(mc)):
    #print getMCKey(mc, n)
    #print getMCVal(mc, n)
    das = "dasgoclient --limit=1 --query=\"file dataset=%s\"" %getMCVal(mc, n)
    #execme(das)

#toPrint("Total single muon DATA samples",len(muData))
for n in range(len(muData)):
    #print getDataKey(muData, n)
    #print getDataVal(muData, n)
    das = "dasgoclient --limit=1 --query=\"file dataset=%s\"" %getDataVal(muData, n)
    #execme(das)

#toPrint("Total single electron DATA samples",len(eleData))
for n in range(len(eleData)):
    #print getDataKey(eleData, n)
    #print getDataVal(eleData, n)
    das = "dasgoclient --limit=1 --query=\"file dataset=%s\"" %getDataVal(eleData, n)
    #execme(das)

#------------------------------------------
#USER INPUTS
#------------------------------------------
#muon channel
isMu = False
isMuMC = False
isMuData = False
range_muMC = len(mc)
range_muData = len(muData)

#electron channel
isEle = True
isEleMC = True
isEleData = True
range_EleMC = len(mc)
range_EleData = len(eleData)

#------------------------------------------
#CRAB PARAMETERS
#------------------------------------------
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#default CRAB parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
#config.Data.unitsPerJob = 10
config.JobType.maxMemoryMB = 4000
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'
config.JobType.inputFiles = ["../../MiniTree/Selection/test/Spring16_25nsV10_MC_PtResolution_AK4PF.txt", "../../MiniTree/Selection/test/Spring16_25nsV10_MC_SF_AK4PF.txt"]

date = str(datetime.date.today()).replace("-","")
muMC_T2Paths_ = open("ntupleT2Paths_muMC"+ date +".txt", 'w')
muData_T2Paths_ = open("ntupleT2Paths_muData"+ date +".txt", 'w')
all_T2Paths = open("ntupleT2Paths_"+ date +".txt", 'w')

#------------------------------------------
#MUON CHANNEL
#------------------------------------------
muMC_T2Paths = ["MUON MC:"]
muData_T2Paths = ["MUON DATA:"]
muMC_dirT2 = "ntuple_MuMC_kfitM_"+date
muData_dirT2 = "ntuple_MuData_kfitM_"+date
if isMu:
    if isMuMC:
        #toPrint("MUONS, MC ","")
        for m in range(range_muMC):
            mu_MC = "MuMC_"+ date
            config.Data.splitting = 'FileBased'
            if("ST" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            elif("TTJetsM" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 2
            elif("TTJetsP" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            elif("Hplus" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            else:
                config.Data.unitsPerJob = 8
            createMuMCpsetFile(mu_MC, "../../MiniTree/Selection/test/muonNtuple_cfg.py", mc, m)
            config.General.requestName = getMCKey(mc, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mc, m)
            config.Data.outLFNDirBase = getLFNDirBaseMC(mu_MC, mc, m, muMC_dirT2)
            #config.JobType.outputFiles = [getMCKey(mc, m)+ mu_MC+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mc, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muMC_T2Paths.append(getNtupleT2Paths(mu_MC, mc, m, muMC_dirT2))

    if isMuData:
        #toPrint("MUONS, DATA ","")
        for d in range(range_muData):
            mu_Data = "MuData_"+ date
            #mu_Data = "MuData_"+ date
            #config.Data.splitting = 'FileBased'
            #config.Data.unitsPerJob = 300
            config.Data.unitsPerJob = 20
            config.Data.splitting = 'LumiBased'
            config.Data.allowNonValidInputDataset = True
            createMuDatapsetFile(mu_Data, "../../MiniTree/Selection/test/muonNtuple_cfg.py", muData, d)
            config.General.requestName = getDataKey(muData, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            #....................
            crab_dir = "CrabMuData_20171115"
            crab_subdir = "crab_"+getDataKey(muData, d)+"_MuData_"+crab_dir.split("_")[1]
            config.Data.lumiMask = "%s/%s/results/notFinishedLumis.json" % (crab_dir, crab_subdir)
            print config.Data.lumiMask
            #.....................
            #config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt"
            config.Data.inputDataset = getDataVal(muData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(mu_Data, muData, d, muData_dirT2)
            #config.JobType.outputFiles = [getDataKey(muData, d)+ mu_Data+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getDataKey(muData, d)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muData_T2Paths.append(getNtupleT2Paths(mu_Data, muData, d, muData_dirT2))

muMC_T2Paths_.write(str(muMC_T2Paths)+",\n\n")
all_T2Paths.write(str(muMC_T2Paths)+",\n\n")
muData_T2Paths_.write(str(muData_T2Paths)+",\n\n")
all_T2Paths.write(str(muData_T2Paths)+",\n\n")

#------------------------------------------
#ELECTRON CHANNEL
#------------------------------------------
electrons_MC_t2_paths = ["ELECTRON MC:"]
electrons_Data_t2_paths = ["ELECTRON DATA:"]
eleMC_dirT2 = "ntuple_EleMC_kfitM_"+date
eleData_dirT2 = "ntuple_EleData_kfitM_"+date
if isEle:
    if isEleMC:
        #toPrint("ELECTRONS, MC ","")
        for m in range(range_EleMC):
            ele_MC = "EleMC_"+ date
            config.Data.splitting = 'FileBased'
            if("ST" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            elif("TTJetsM" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 2
            elif("TTJetsP" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            elif("Hplus" in getMCKey(mc, m)):
                config.Data.unitsPerJob = 3
            else:
                config.Data.unitsPerJob = 8
            createEleMCpsetFile(ele_MC, "../../MiniTree/Selection/test/electronNtuple_cfg.py", mc, m)
            config.General.requestName = getMCKey(mc, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mc, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(ele_MC, mc, m, eleMC_dirT2)
            #config.JobType.outputFiles = [getMCKey(mc, m)+ ele_MC+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mc, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_MC_t2_paths.append(getNtupleT2Paths(ele_MC, mc, m, eleMC_dirT2))

    if isEleData:
        #toPrint("ELECTRONS, DATA ","")
        for d in range(range_EleData):
            ele_Data = "EleData_"+ date
            #config.Data.unitsPerJob = 20
            config.Data.unitsPerJob = 300
            config.Data.splitting = 'LumiBased'
            config.Data.allowNonValidInputDataset = True
            createEleDatapsetFile(ele_Data, "../../MiniTree/Selection/test/electronNtuple_cfg.py", eleData, d)
            config.General.requestName = getDataKey(eleData, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt"
            config.Data.inputDataset = getDataVal(eleData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(ele_Data, eleData, d, eleData_dirT2)
            #config.JobType.outputFiles = [getDataKey(eleData, d)+ ele_Data+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getDataKey(eleData, d)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_Data_t2_paths.append(getNtupleT2Paths(ele_Data, eleData, d, eleData_dirT2))

#ALL T2 PATHS
all_T2Paths.write(str(electrons_MC_t2_paths)+",\n\n")
all_T2Paths.write(str(electrons_Data_t2_paths))
