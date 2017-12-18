import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Charged Higgs & Bkg at 13 TeV
run = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
year = run+"-v1"
yext1_v1 = run +"_ext1-v1"
yext1_v2 = run +"_ext1-v2"
M = "/MINIAODSIM"

mcSampDict_ ={
        "TTJetsM": "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "TTJetsP": "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_up": "/TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_down": "/TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampUP": "/TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampDOWN": "/TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "ST_tW": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_t": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_s": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+year+M,
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
        "WW": "/WW_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "WZ": "/WZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "ZZ": "/ZZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "HplusM80": "/ChargedHiggsToCS_M080_13TeV-madgraph/"+year+M,
        "HplusM90": "/ChargedHiggsToCS_M090_13TeV-madgraph/"+year+M,
        "HplusM100": "/ChargedHiggsToCS_M100_13TeV-madgraph/"+year+M,
        "HplusM120": "/ChargedHiggsToCS_M120_13TeV-madgraph/"+year+M,
        "HplusM140": "/ChargedHiggsToCS_M140_13TeV-madgraph/"+year+M,
        "HplusM150": "/ChargedHiggsToCS_M150_13TeV-madgraph/"+year+M,
        "HplusM155": "/ChargedHiggsToCS_M155_13TeV-madgraph/"+year+M,
        "HplusM160": "/ChargedHiggsToCS_M160_13TeV-madgraph/"+year+M
        }
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

#Other ttbar samples
'''
mcSampDict_ ={
        "TTJetsP_isrup": "/TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8/"+yext1_v1+M,
        "TTJetsP_fsrup": "/TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8/"+year+M,
        "TTJetsP_isrdown": "/TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8/"+year+M,
        "TTJetsP_fsrdown": "/TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8/"+year+M,
        }
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))
'''
