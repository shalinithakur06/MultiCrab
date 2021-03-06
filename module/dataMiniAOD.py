import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

#All Data Samples at 13 TeV
muDataSampDict_ ={
        "MuRunB2v2": "/DoubleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD",
        "MuRunCv1":  "/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD",
        "MuRunDv1":  "/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD",
        "MuRunEv1":  "/DoubleMuon/Run2016E-03Feb2017-v1/MINIAOD",
        "MuRunFv1":  "/DoubleMuon/Run2016F-03Feb2017-v1/MINIAOD",
        "MuRunGv1":  "/DoubleMuon/Run2016G-03Feb2017-v1/MINIAOD",
        "MuRunH2v1": "/DoubleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD",
        "MuRunH3v1": "/DoubleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"
         }
muDataSampDict= OrderedDict(sorted(muDataSampDict_.items(), key=lambda t: t[0]))


eleDataSampDict_ ={
        "EleRunBver2v2": "/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD",
        "EleRunCv1":     "/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD",
        "EleRunDv1": 	 "/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD",
        "EleRunEv1": 	 "/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD",
        "EleRunFv1": 	 "/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD",
        "EleRunGv1":  	 "/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD",
        "EleRunHver2v1": "/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD"
         }
eleDataSampDict= OrderedDict(sorted(eleDataSampDict_.items(), key=lambda t: t[0]))








