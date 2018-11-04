import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Excited Lepton & Bkg at 13 TeV
RUN = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
M = "MINIAODSIM"

#### Both channel
mcSampDict_ = {"DYJetsToLL_M50":"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext2-v1/"+M}
mcSampDict_["DYJetsToLL_M50"]="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext2-v1/"+M
mcSampDict_["DYJetsToLL_M100to200"]="/DYJetsToLL_M-100to200_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M200to400"]="/DYJetsToLL_M-200to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["DYJetsToLL_M400to500"]="/DYJetsToLL_M-400to500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M500to700"]="/DYJetsToLL_M-500to700_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M700to800"]="/DYJetsToLL_M-700to800_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M800to1000"]="/DYJetsToLL_M-800to1000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M1000to1500"]="/DYJetsToLL_M-1000to1500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M1500to2000"]="/DYJetsToLL_M-1500to2000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["DYJetsToLL_M2000to3000"]="/DYJetsToLL_M-2000to3000_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M
mcSampDict_["TT"]="/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WJetsToLNu"]="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WW"]="/WW_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WZ"]="/WZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ZZ"]="/ZZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M

'''
# Add muon signal samples to the dictionary
mcSampDict_ = {"ExLepMuMuZ_M250":"/ExcitedLepton_MuMuZ-250_TuneCUETP8M1_13TeV_pythia8/"+RUN+"-v2/"+M}
#mcSampDict_["ExLepMuMuZ_M250"]="/ExcitedLepton_MuMuZ-250_TuneCUETP8M1_13TeV_pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M1500"]="/ExcitedLepton_MuMuZ-1500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepMuMuZ_M2000"]="/ExcitedLepton_MuMuZ-2000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M2500"]="/ExcitedLepton_MuMuZ-2500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M4000"]="/ExcitedLepton_MuMuZ-4000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
'''

# Add electron signal samples to the dictionary
#mcSampDict_={"ExLepEEZ_M250":"/ExcitedLepton_EEZ-250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M}
mcSampDict_["ExLepEEZ_M250"]="/ExcitedLepton_EEZ-250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M2000"]="/ExcitedLepton_EEZ-2000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepEEZ_M2500"]="/ExcitedLepton_EEZ-2500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M4000"]="/ExcitedLepton_EEZ-4000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M

# Finally, sort dictionaly w.r.t the keys
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

