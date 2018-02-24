import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Charged Higgs & Bkg at 13 TeV
run = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
year = run+"-v1"
yext1_v1 = run +"_ext1-v1"
yext1_v2 = run +"_ext1-v2"
M = "/MINIAODSIM"

mcSampDict_ ={
		"TestLHEGeneration_Mu_2000": "/TestLHEGeneration_Mu/sthakur-MCGenerationStep5_Mu2000_2018_1_27-652b8f7cd5d2b9159ac64422f0aacee9/USER",
		"TestLHEGeneration_Mu_4000": "/TestLHEGeneration_Mu/sthakur-MCGenerationStep5_Mu4000_2018_1_27-652b8f7cd5d2b9159ac64422f0aacee9/USER",
		"TestLHEGeneration_Mu_6000": "/TestLHEGeneration_Mu/sthakur-MCGenerationStep5_Mu6000_2018_1_27-652b8f7cd5d2b9159ac64422f0aacee9/USER"
	}
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

'''
mcSampDict_ ={
        "TTJetsP": "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "WJetsToLNu": "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W1JetsToLNu": "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W2JetsToLNu": "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W3JetsToLNu": "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W4JetsToLNu": "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DYJetsToLL": "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+yext1_v2+M,
        "DY1JetsToLL": "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY2JetsToLL": "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY3JetsToLL": "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY4JetsToLL": "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "QCD_Pt-15to20_Mu": "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-20to30_Mu": "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-30to50_Mu": "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-50to80_Mu": "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-80to120_Mu": "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-120to170_Mu": "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-170to300_Mu": "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-300to470_Mu": "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-470to600_Mu": "/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-600to800_Mu": "/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-800to1000_Mu": "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-1000toInf_Mu": "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "WW": "/WW_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "WZ": "/WZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "ZZ": "/ZZ_TuneCUETP8M1_13TeV-pythia8/"+year+M
        }
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))
'''
