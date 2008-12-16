import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *

source = cms.Source("MadGraphSource",
    ## DEFAULT SETTINGS
    # parameters related to ME-PS matching
    produceEventTreeFile = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    # turn to standard sources way of inputting filename
    # these events need to be generated begore
    fileNames = cms.untracked.vstring('file:/path_to_specific_madgraph/ggH_10TeV_unweighted_events.lhe'),
    #MEMAIN_qcut = cms.untracked.double(15.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    # values for the MEMAIN routine (matching).
    # if set to 0. default values will be chosen from the interface
    # MEMAIN_etaclmax = cms.untracked.double(5.0),
    # for reading non-MG LHE files
    minimalLH = cms.untracked.bool(False),
    # general parameters
    firstEvent = cms.untracked.uint32(0),
    # only set to 1 if need to perform exclusive matching
    MEMAIN_iexcfile = cms.untracked.uint32(0), 

    maxEventsToPrint = cms.untracked.int32(0),
    # for reading from castor
    getInputFromMCDB = cms.untracked.bool(False),
    MCDBArticleID = cms.int32(0),
    ############################################################
    # PYTHIA
    ############################################################
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        pythiaCMSDefaults = cms.vstring(
            'PMAS(5,1)=4.4  ! b quarks mass', 
            'PMAS(6,1)=175  ! t quarks mass', 
            'MSTJ(1)=1      !...Fragmentation/hadronization on or off', 
            'MSTP(61)=1     ! Parton showering on or off', 
            'MSTP(143)=1    ! MUST BE 1 FOR THE MATCHING ROUTINE TO RUN!!!!', 
            'MSEL=0         ! User defined processes/Full user control'),
        # This is a vector of ParameterSet names to be read, in this order
        # The first is general default pythia parameters, the second are own
        # additions
        parameterSets = cms.vstring('pythiaUESettings', 
            'pythiaCMSDefaults')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 0.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/MadGraph_PYTHIA6_SM_WWNjets_2l2nuNjets_10TeV_cff.py,v $'),
    annotation = cms.untracked.string(
    'MadGraph Pythia6 SM WWNjets->2l2nuNjets at 10TeV')
)
 

