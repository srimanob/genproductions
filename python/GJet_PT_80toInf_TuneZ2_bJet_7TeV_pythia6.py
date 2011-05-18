import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(7000.0),
	crossSection = cms.untracked.double(3.321052e-01),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 10        ! prompt photon processes',
			'CKIN(3) = 80     ! minimum pt hat for hard interactions',
#			'CKIN(4) = 1400  ! maximum pt hat for hard interactions',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
		)
	)
)

heavyflavorjetfilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(5, -5)
)

ProductionFilterSequence = cms.Sequence(generator*heavyflavorjetfilter)

