import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Excited Lepton & Bkg at 13 TeV
RUN = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
M = "MINIAODSIM"

#### Both channel
mcSampDict_ = {"DYJetsToLL_M50":"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext2-v1/"+M}
mcSampDict_["DYJetsToLL_Pt50To100"]="/DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v3/"+M
mcSampDict_["DYJetsToLL_Pt100To250"]="/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v2/"+M
mcSampDict_["DYJetsToLL_Pt250To400"]="/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["DYJetsToLL_Pt400To650"]="/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["DYJetsToLL_Pt650ToInf"]="/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
mcSampDict_["TT"]="/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WJetsToLNu"]="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WW"]="/WW_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["WZ"]="/WZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ZZ"]="/ZZ_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v1/"+M

# Add muon signal samples to the dictionary
'''
#mcSampDict_ = {"ExLepMuMuZ_M250":"/ExcitedLepton_MuMuZ-250_TuneCUETP8M1_13TeV_pythia8/"+RUN+"-v2/"+M}
mcSampDict_["ExLepMuMuZ_M250"]="/ExcitedLepton_MuMuZ-250_TuneCUETP8M1_13TeV_pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M500"]="/ExcitedLepton_MuMuZ-500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M750"]="/ExcitedLepton_MuMuZ-750_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M1000"]="/ExcitedLepton_MuMuZ-1000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M1250"]="/ExcitedLepton_MuMuZ-1250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M1500"]="/ExcitedLepton_MuMuZ-1500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepMuMuZ_M1750"]="/ExcitedLepton_MuMuZ-1750_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M2000"]="/ExcitedLepton_MuMuZ-2000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M2500"]="/ExcitedLepton_MuMuZ-2500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M3000"]="/ExcitedLepton_MuMuZ-3000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M3500"]="/ExcitedLepton_MuMuZ-3500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M4000"]="/ExcitedLepton_MuMuZ-4000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepMuMuZ_M4500"]="/ExcitedLepton_MuMuZ-4500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepMuMuZ_M5000"]="/ExcitedLepton_MuMuZ-5000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
'''

# Add electron signal samples to the dictionary
#mcSampDict_={"ExLepEEZ_M250":"/ExcitedLepton_EEZ-250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M}
mcSampDict_["ExLepEEZ_M250"]="/ExcitedLepton_EEZ-250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepEEZ_M500"]="/ExcitedLepton_EEZ-500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M750"]="/ExcitedLepton_EEZ-750_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M1000"]="/ExcitedLepton_EEZ-1000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M1250"]="/ExcitedLepton_EEZ-1250_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M1500"]="/ExcitedLepton_EEZ-1500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M1750"]="/ExcitedLepton_EEZ-1750_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M2000"]="/ExcitedLepton_EEZ-2000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepEEZ_M2500"]="/ExcitedLepton_EEZ-2500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M3000"]="/ExcitedLepton_EEZ-3000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M3500"]="/ExcitedLepton_EEZ-3500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M4000"]="/ExcitedLepton_EEZ-4000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v3/"+M
mcSampDict_["ExLepEEZ_M4500"]="/ExcitedLepton_EEZ-4500_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M
mcSampDict_["ExLepEEZ_M5000"]="/ExcitedLepton_EEZ-5000_TuneCUETP8M1_13TeV-pythia8/"+RUN+"-v2/"+M

# Finally, sort dictionaly w.r.t the keys
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

