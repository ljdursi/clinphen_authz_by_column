"""
SQLAlchemy models for the clin/phen service
"""
from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Announcement(Base):
    __tablename__ = 'announcement'

    id = Column(Integer, primary_key=True)
    attributes = Column(Text)
    url = Column(Text, nullable=False)
    remote_addr = Column(Text)
    user_agent = Column(Text)
    created = Column(DateTime, nullable=False)


class Dataset(Base):
    __tablename__ = 'dataset'

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    description = Column(Text)
    info = Column(Text)
    name = Column(Text, nullable=False, unique=True)


class Ontology(Base):
    __tablename__ = 'ontology'

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    name = Column(Text, nullable=False, unique=True)
    ontologyPrefix = Column(Text, nullable=False)


class Peer(Base):
    __tablename__ = 'peer'

    url = Column(Text, primary_key=True)
    attributes = Column(Text)


class Referenceset(Base):
    __tablename__ = 'referenceset'

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    assemblyId = Column(Text)
    dataUrl = Column(Text, nullable=False)
    description = Column(Text)
    isDerived = Column(Integer)
    md5checksum = Column(Text)
    name = Column(Text, nullable=False, unique=True)
    species = Column(Text)
    sourceAccessions = Column(Text)
    sourceUri = Column(Text)


class System(Base):
    __tablename__ = 'system'

    key = Column(Text, primary_key=True)
    attributes = Column(Text)
    value = Column(Text, nullable=False)


class Alignment(Base):
    __tablename__ = 'alignment'
    __table_args__ = (
        Index('alignment_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    alignmentId = Column(Text)
    alignmentIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    inHousePipeline = Column(Text)
    inHousePipelineTier = Column(Integer)
    alignmentTool = Column(Text)
    alignmentToolTier = Column(Integer)
    mergeTool = Column(Text)
    mergeToolTier = Column(Integer)
    markDuplicates = Column(Text)
    markDuplicatesTier = Column(Integer)
    realignerTarget = Column(Text)
    realignerTargetTier = Column(Integer)
    indelRealigner = Column(Text)
    indelRealignerTier = Column(Integer)
    baseRecalibrator = Column(Text)
    baseRecalibratorTier = Column(Integer)
    printReads = Column(Text)
    printReadsTier = Column(Integer)
    idxStats = Column(Text)
    idxStatsTier = Column(Integer)
    flagStat = Column(Text)
    flagStatTier = Column(Integer)
    coverage = Column(Text)
    coverageTier = Column(Integer)
    insertSizeMetrics = Column(Text)
    insertSizeMetricsTier = Column(Integer)
    fastqc = Column(Text)
    fastqcTier = Column(Integer)
    reference = Column(Text)
    referenceTier = Column(Integer)
    sequencingId = Column(Text)
    sequencingIdTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Analysi(Base):
    __tablename__ = 'analysis'

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text)
    created = Column(Text)
    updated = Column(Text)
    analysistype = Column(Text)
    software = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    experimentId = Column(Text)
    other_analysis_descriptor = Column(Text)
    other_analysis_completition_date = Column(Text)

    dataset = relationship('Dataset')


class Biosample(Base):
    __tablename__ = 'biosample'
    __table_args__ = (
        Index('biosample_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    created = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    description = Column(Text)
    disease = Column(Text)
    individualId = Column(Text, nullable=False)
    info = Column(Text)
    name = Column(Text, nullable=False)
    updated = Column(Text)
    individualAgeAtCollection = Column(Text)
    estimated_tumor_content = Column(Text)
    normal_sample_source = Column(Text)
    biopsy_data = Column(Text)
    tumor_biopsy_anatomical_site = Column(Text)
    biopsy_type = Column(Text)
    sample_shipment_date = Column(Text)

    dataset = relationship('Dataset')


class Celltransplant(Base):
    __tablename__ = 'celltransplant'
    __table_args__ = (
        Index('celltransplant_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    cellSource = Column(Text)
    cellSourceTier = Column(Integer)
    donorType = Column(Text)
    donorTypeTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)

    dataset = relationship('Dataset')


class Chemotherapy(Base):
    __tablename__ = 'chemotherapy'
    __table_args__ = (
        Index('chemotherapy_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    stopDate = Column(Text)
    stopDateTier = Column(Integer)
    systematicTherapyAgentName = Column(Text)
    systematicTherapyAgentNameTier = Column(Integer)
    route = Column(Text)
    routeTier = Column(Integer)
    dose = Column(Text)
    doseTier = Column(Integer)
    doseFrequency = Column(Text)
    doseFrequencyTier = Column(Integer)
    doseUnit = Column(Text)
    doseUnitTier = Column(Integer)
    daysPerCycle = Column(Text)
    daysPerCycleTier = Column(Integer)
    numberOfCycle = Column(Text)
    numberOfCycleTier = Column(Integer)
    treatmentIntent = Column(Text)
    treatmentIntentTier = Column(Integer)
    treatingCentreName = Column(Text)
    treatingCentreNameTier = Column(Integer)
    type = Column(Text)
    typeTier = Column(Integer)
    protocolCode = Column(Text)
    protocolCodeTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)

    dataset = relationship('Dataset')


class Complication(Base):
    __tablename__ = 'complication'
    __table_args__ = (
        Index('complication_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    date = Column(Text)
    dateTier = Column(Integer)
    lateComplicationOfTherapyDeveloped = Column(Text)
    lateComplicationOfTherapyDevelopedTier = Column(Integer)
    lateToxicityDetail = Column(Text)
    lateToxicityDetailTier = Column(Integer)
    suspectedTreatmentInducedNeoplasmDeveloped = Column(Text)
    suspectedTreatmentInducedNeoplasmDevelopedTier = Column(Integer)
    treatmentInducedNeoplasmDetails = Column(Text)
    treatmentInducedNeoplasmDetailsTier = Column(Integer)

    dataset = relationship('Dataset')


class Consent(Base):
    __tablename__ = 'consent'
    __table_args__ = (
        Index('consent_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    consentId = Column(Text)
    consentIdTier = Column(Integer)
    consentDate = Column(Text)
    consentDateTier = Column(Integer)
    consentVersion = Column(Text)
    consentVersionTier = Column(Integer)
    patientConsentedTo = Column(Text)
    patientConsentedToTier = Column(Integer)
    reasonForRejection = Column(Text)
    reasonForRejectionTier = Column(Integer)
    wasAssentObtained = Column(Text)
    wasAssentObtainedTier = Column(Integer)
    dateOfAssent = Column(Text)
    dateOfAssentTier = Column(Integer)
    assentFormVersion = Column(Text)
    assentFormVersionTier = Column(Integer)
    ifAssentNotObtainedWhyNot = Column(Text)
    ifAssentNotObtainedWhyNotTier = Column(Integer)
    reconsentDate = Column(Text)
    reconsentDateTier = Column(Integer)
    reconsentVersion = Column(Text)
    reconsentVersionTier = Column(Integer)
    consentingCoordinatorName = Column(Text)
    consentingCoordinatorNameTier = Column(Integer)
    previouslyConsented = Column(Text)
    previouslyConsentedTier = Column(Integer)
    nameOfOtherBiobank = Column(Text)
    nameOfOtherBiobankTier = Column(Integer)
    hasConsentBeenWithdrawn = Column(Text)
    hasConsentBeenWithdrawnTier = Column(Integer)
    dateOfConsentWithdrawal = Column(Text)
    dateOfConsentWithdrawalTier = Column(Integer)
    typeOfConsentWithdrawal = Column(Text)
    typeOfConsentWithdrawalTier = Column(Integer)
    reasonForConsentWithdrawal = Column(Text)
    reasonForConsentWithdrawalTier = Column(Integer)
    consentFormComplete = Column(Text)
    consentFormCompleteTier = Column(Integer)

    dataset = relationship('Dataset')


class Continuousset(Base):
    __tablename__ = 'continuousset'
    __table_args__ = (
        Index('continuousset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    info = Column(Text)
    name = Column(Text, nullable=False)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)
    sourceUri = Column(Text)

    dataset = relationship('Dataset')
    referenceset = relationship('Referenceset')


class Diagnosi(Base):
    __tablename__ = 'diagnosis'
    __table_args__ = (
        Index('diagnosis_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    diagnosisId = Column(Text)
    diagnosisIdTier = Column(Integer)
    diagnosisDate = Column(Text)
    diagnosisDateTier = Column(Integer)
    ageAtDiagnosis = Column(Text)
    ageAtDiagnosisTier = Column(Integer)
    cancerType = Column(Text)
    cancerTypeTier = Column(Integer)
    classification = Column(Text)
    classificationTier = Column(Integer)
    cancerSite = Column(Text)
    cancerSiteTier = Column(Integer)
    histology = Column(Text)
    histologyTier = Column(Integer)
    methodOfDefinitiveDiagnosis = Column(Text)
    methodOfDefinitiveDiagnosisTier = Column(Integer)
    sampleType = Column(Text)
    sampleTypeTier = Column(Integer)
    sampleSite = Column(Text)
    sampleSiteTier = Column(Integer)
    tumorGrade = Column(Text)
    tumorGradeTier = Column(Integer)
    gradingSystemUsed = Column(Text)
    gradingSystemUsedTier = Column(Integer)
    sitesOfMetastases = Column(Text)
    sitesOfMetastasesTier = Column(Integer)
    stagingSystem = Column(Text)
    stagingSystemTier = Column(Integer)
    versionOrEditionOfTheStagingSystem = Column(Text)
    versionOrEditionOfTheStagingSystemTier = Column(Integer)
    specificTumorStageAtDiagnosis = Column(Text)
    specificTumorStageAtDiagnosisTier = Column(Integer)
    prognosticBiomarkers = Column(Text)
    prognosticBiomarkersTier = Column(Integer)
    biomarkerQuantification = Column(Text)
    biomarkerQuantificationTier = Column(Integer)
    additionalMolecularTesting = Column(Text)
    additionalMolecularTestingTier = Column(Integer)
    additionalTestType = Column(Text)
    additionalTestTypeTier = Column(Integer)
    laboratoryName = Column(Text)
    laboratoryNameTier = Column(Integer)
    laboratoryAddress = Column(Text)
    laboratoryAddressTier = Column(Integer)
    siteOfMetastases = Column(Text)
    siteOfMetastasesTier = Column(Integer)
    stagingSystemVersion = Column(Text)
    stagingSystemVersionTier = Column(Integer)
    specificStage = Column(Text)
    specificStageTier = Column(Integer)
    cancerSpecificBiomarkers = Column(Text)
    cancerSpecificBiomarkersTier = Column(Integer)
    additionalMolecularDiagnosticTestingPerformed = Column(Text)
    additionalMolecularDiagnosticTestingPerformedTier = Column(Integer)
    additionalTest = Column(Text)
    additionalTestTier = Column(Integer)

    dataset = relationship('Dataset')


class Enrollment(Base):
    __tablename__ = 'enrollment'
    __table_args__ = (
        Index('enrollment_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    enrollmentInstitution = Column(Text)
    enrollmentInstitutionTier = Column(Integer)
    enrollmentApprovalDate = Column(Text)
    enrollmentApprovalDateTier = Column(Integer)
    crossEnrollment = Column(Text)
    crossEnrollmentTier = Column(Integer)
    otherPersonalizedMedicineStudyName = Column(Text)
    otherPersonalizedMedicineStudyNameTier = Column(Integer)
    otherPersonalizedMedicineStudyId = Column(Text)
    otherPersonalizedMedicineStudyIdTier = Column(Integer)
    ageAtEnrollment = Column(Text)
    ageAtEnrollmentTier = Column(Integer)
    eligibilityCategory = Column(Text)
    eligibilityCategoryTier = Column(Integer)
    statusAtEnrollment = Column(Text)
    statusAtEnrollmentTier = Column(Integer)
    primaryOncologistName = Column(Text)
    primaryOncologistNameTier = Column(Integer)
    primaryOncologistContact = Column(Text)
    primaryOncologistContactTier = Column(Integer)
    referringPhysicianName = Column(Text)
    referringPhysicianNameTier = Column(Integer)
    referringPhysicianContact = Column(Text)
    referringPhysicianContactTier = Column(Integer)
    summaryOfIdRequest = Column(Text)
    summaryOfIdRequestTier = Column(Integer)
    treatingCentreName = Column(Text)
    treatingCentreNameTier = Column(Integer)
    treatingCentreProvince = Column(Text)
    treatingCentreProvinceTier = Column(Integer)

    dataset = relationship('Dataset')



class Experiment(Base):
    __tablename__ = 'experiment'

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text)
    created = Column(Text)
    updated = Column(Text)
    runTime = Column(Text)
    molecule = Column(Text)
    strategy = Column(Text)
    selection = Column(Text)
    library = Column(Text)
    libraryLayout = Column(Text)
    instrumentModel = Column(Text)
    instrumentDataFile = Column(Text)
    sequencingCenter = Column(Text)
    platformUnit = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    biosampleId = Column(Text)
    dna_library_construction_method = Column(Text)
    wgs_sequencing_completion_date = Column(Text)
    rna_library_construction_method = Column(Text)
    rna_sequencing_completion_date = Column(Text)
    panel_completion_date = Column(Text)

    dataset = relationship('Dataset')


class Expressionanalysi(Base):
    __tablename__ = 'expressionanalysis'
    __table_args__ = (
        Index('expressionanalysis_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    expressionAnalysisId = Column(Text)
    expressionAnalysisIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    readLength = Column(Text)
    readLengthTier = Column(Integer)
    reference = Column(Text)
    referenceTier = Column(Integer)
    alignmentTool = Column(Text)
    alignmentToolTier = Column(Integer)
    bamHandling = Column(Text)
    bamHandlingTier = Column(Integer)
    expressionEstimation = Column(Text)
    expressionEstimationTier = Column(Integer)
    sequencingId = Column(Text)
    sequencingIdTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Extraction(Base):
    __tablename__ = 'extraction'
    __table_args__ = (
        Index('extraction_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    extractionId = Column(Text)
    extractionIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    rnaBlood = Column(Text)
    rnaBloodTier = Column(Integer)
    dnaBlood = Column(Text)
    dnaBloodTier = Column(Integer)
    rnaTissue = Column(Text)
    rnaTissueTier = Column(Integer)
    dnaTissue = Column(Text)
    dnaTissueTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Featureset(Base):
    __tablename__ = 'featureset'
    __table_args__ = (
        Index('featureset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    info = Column(Text)
    name = Column(Text, nullable=False)
    ontologyId = Column(ForeignKey('ontology.id'), nullable=False, index=True)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)
    sourceUri = Column(Text)

    dataset = relationship('Dataset')
    ontology = relationship('Ontology')
    referenceset = relationship('Referenceset')


class Fusiondetection(Base):
    __tablename__ = 'fusiondetection'
    __table_args__ = (
        Index('fusiondetection_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    fusionDetectionId = Column(Text)
    fusionDetectionIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    inHousePipeline = Column(Text)
    inHousePipelineTier = Column(Integer)
    svDetection = Column(Text)
    svDetectionTier = Column(Integer)
    fusionDetection = Column(Text)
    fusionDetectionTier = Column(Integer)
    realignment = Column(Text)
    realignmentTier = Column(Integer)
    annotation = Column(Text)
    annotationTier = Column(Integer)
    genomeReference = Column(Text)
    genomeReferenceTier = Column(Integer)
    geneModels = Column(Text)
    geneModelsTier = Column(Integer)
    alignmentId = Column(Text)
    alignmentIdTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Immunotherapy(Base):
    __tablename__ = 'immunotherapy'
    __table_args__ = (
        Index('immunotherapy_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    immunotherapyType = Column(Text)
    immunotherapyTypeTier = Column(Integer)
    immunotherapyTarget = Column(Text)
    immunotherapyTargetTier = Column(Integer)
    immunotherapyDetail = Column(Text)
    immunotherapyDetailTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)

    dataset = relationship('Dataset')


class Individual(Base):
    __tablename__ = 'individual'
    __table_args__ = (
        Index('individual_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    created = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    description = Column(Text)
    info = Column(Text)
    name = Column(Text)
    sex = Column(Text)
    species = Column(Text)
    updated = Column(Text)
    patient_id = Column(Text)
    regional_profiling_centre = Column(Text)
    diagnosis = Column(Text)
    pathology_type = Column(Text)
    enrollment_approval_date = Column(Text)
    enrollment_approval_initials = Column(Text)
    date_of_upload_to_sFTP = Column(Text)
    tumor_board_presentation_date_and_analyses = Column(Text)
    comments = Column(Text)

    dataset = relationship('Dataset')


class Labtest(Base):
    __tablename__ = 'labtest'
    __table_args__ = (
        Index('labtest_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    collectionDate = Column(Text)
    collectionDateTier = Column(Integer)
    endDate = Column(Text)
    endDateTier = Column(Integer)
    eventType = Column(Text)
    eventTypeTier = Column(Integer)
    testResults = Column(Text)
    testResultsTier = Column(Integer)
    timePoint = Column(Text)
    timePointTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)

    dataset = relationship('Dataset')


class Outcome(Base):
    __tablename__ = 'outcome'
    __table_args__ = (
        Index('outcome_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    physicalExamId = Column(Text)
    physicalExamIdTier = Column(Integer)
    dateOfAssessment = Column(Text)
    dateOfAssessmentTier = Column(Integer)
    diseaseResponseOrStatus = Column(Text)
    diseaseResponseOrStatusTier = Column(Integer)
    otherResponseClassification = Column(Text)
    otherResponseClassificationTier = Column(Integer)
    minimalResidualDiseaseAssessment = Column(Text)
    minimalResidualDiseaseAssessmentTier = Column(Integer)
    methodOfResponseEvaluation = Column(Text)
    methodOfResponseEvaluationTier = Column(Integer)
    responseCriteriaUsed = Column(Text)
    responseCriteriaUsedTier = Column(Integer)
    summaryStage = Column(Text)
    summaryStageTier = Column(Integer)
    sitesOfAnyProgressionOrRecurrence = Column(Text)
    sitesOfAnyProgressionOrRecurrenceTier = Column(Integer)
    vitalStatus = Column(Text)
    vitalStatusTier = Column(Integer)
    height = Column(Text)
    heightTier = Column(Integer)
    weight = Column(Text)
    weightTier = Column(Integer)
    heightUnits = Column(Text)
    heightUnitsTier = Column(Integer)
    weightUnits = Column(Text)
    weightUnitsTier = Column(Integer)
    performanceStatus = Column(Text)
    performanceStatusTier = Column(Integer)
    overallSurvivalInMonths = Column(Text)
    overallSurvivalInMonthsTier = Column(Integer)
    diseaseFreeSurvivalInMonths = Column(Text)
    diseaseFreeSurvivalInMonthsTier = Column(Integer)
    siteOfRelapseOrProgression = Column(Text)
    siteOfRelapseOrProgressionTier = Column(Integer)
    intervalProgressionOrRecurrence = Column(Text)
    intervalProgressionOrRecurrenceTier = Column(Integer)
    intervalRegressionOrDecreaseInDisease = Column(Text)
    intervalRegressionOrDecreaseInDiseaseTier = Column(Integer)
    levelOfMalignancy = Column(Text)
    levelOfMalignancyTier = Column(Integer)
    treatmentInducedNeoplasmSite = Column(Text)
    treatmentInducedNeoplasmSiteTier = Column(Integer)
    dateOfDiagnosisOfTreatmentInducedNeoplasm = Column(Text)
    dateOfDiagnosisOfTreatmentInducedNeoplasmTier = Column(Integer)

    dataset = relationship('Dataset')


class Patient(Base):
    __tablename__ = 'patient'
    __table_args__ = (
        Index('patient_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    otherIds = Column(Text)
    otherIdsTier = Column(Integer)
    dateOfBirth = Column(Text)
    dateOfBirthTier = Column(Integer)
    gender = Column(Text)
    genderTier = Column(Integer)
    ethnicity = Column(Text)
    ethnicityTier = Column(Integer)
    race = Column(Text)
    raceTier = Column(Integer)
    provinceOfResidence = Column(Text)
    provinceOfResidenceTier = Column(Integer)
    dateOfDeath = Column(Text)
    dateOfDeathTier = Column(Integer)
    causeOfDeath = Column(Text)
    causeOfDeathTier = Column(Integer)
    autopsyTissueForResearch = Column(Text)
    autopsyTissueForResearchTier = Column(Integer)
    priorMalignancy = Column(Text)
    priorMalignancyTier = Column(Integer)
    dateOfPriorMalignancy = Column(Text)
    dateOfPriorMalignancyTier = Column(Integer)
    familyHistoryAndRiskFactors = Column(Text)
    familyHistoryAndRiskFactorsTier = Column(Integer)
    familyHistoryOfPredispositionSyndrome = Column(Text)
    familyHistoryOfPredispositionSyndromeTier = Column(Integer)
    detailsOfPredispositionSyndrome = Column(Text)
    detailsOfPredispositionSyndromeTier = Column(Integer)
    geneticCancerSyndrome = Column(Text)
    geneticCancerSyndromeTier = Column(Integer)
    otherGeneticConditionOrSignificantComorbidity = Column(Text)
    otherGeneticConditionOrSignificantComorbidityTier = Column(Integer)
    occupationalOrEnvironmentalExposure = Column(Text)
    occupationalOrEnvironmentalExposureTier = Column(Integer)

    dataset = relationship('Dataset')


class Phenotypeassociationset(Base):
    __tablename__ = 'phenotypeassociationset'
    __table_args__ = (
        Index('phenotypeassociationset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    name = Column(Text)

    dataset = relationship('Dataset')


class Radiotherapy(Base):
    __tablename__ = 'radiotherapy'
    __table_args__ = (
        Index('radiotherapy_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    stopDate = Column(Text)
    stopDateTier = Column(Integer)
    therapeuticModality = Column(Text)
    therapeuticModalityTier = Column(Integer)
    baseline = Column(Text)
    baselineTier = Column(Integer)
    testResult = Column(Text)
    testResultTier = Column(Integer)
    testResultStd = Column(Text)
    testResultStdTier = Column(Integer)
    treatingCentreName = Column(Text)
    treatingCentreNameTier = Column(Integer)
    startIntervalRad = Column(Text)
    startIntervalRadTier = Column(Integer)
    startIntervalRadRaw = Column(Text)
    startIntervalRadRawTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)
    adjacentFields = Column(Text)
    adjacentFieldsTier = Column(Integer)
    adjacentFractions = Column(Text)
    adjacentFractionsTier = Column(Integer)
    complete = Column(Text)
    completeTier = Column(Integer)
    brachytherapyDose = Column(Text)
    brachytherapyDoseTier = Column(Integer)
    radiotherapyDose = Column(Text)
    radiotherapyDoseTier = Column(Integer)
    siteNumber = Column(Text)
    siteNumberTier = Column(Integer)
    technique = Column(Text)
    techniqueTier = Column(Integer)
    treatedRegion = Column(Text)
    treatedRegionTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)
    radiationType = Column(Text)
    radiationTypeTier = Column(Integer)
    radiationSite = Column(Text)
    radiationSiteTier = Column(Integer)
    totalDose = Column(Text)
    totalDoseTier = Column(Integer)
    boostSite = Column(Text)
    boostSiteTier = Column(Integer)
    boostDose = Column(Text)
    boostDoseTier = Column(Integer)

    dataset = relationship('Dataset')


class Readgroupset(Base):
    __tablename__ = 'readgroupset'
    __table_args__ = (
        Index('readgroupset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    indexFile = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    programs = Column(Text)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)
    stats = Column(Text, nullable=False)
    patientId = Column(Text, nullable=False)
    sampleId = Column(Text, nullable=False)

    dataset = relationship('Dataset')
    referenceset = relationship('Referenceset')


class Reference(Base):
    __tablename__ = 'reference'
    __table_args__ = (
        Index('reference_referenceSetId_name', 'referenceSetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    isDerived = Column(Integer)
    length = Column(Integer)
    md5checksum = Column(Text)
    name = Column(Text, nullable=False)
    species = Column(Text)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)
    sourceAccessions = Column(Text)
    sourceDivergence = Column(Float)
    sourceUri = Column(Text)

    referenceset = relationship('Referenceset')


class Rnaquantificationset(Base):
    __tablename__ = 'rnaquantificationset'
    __table_args__ = (
        Index('rnaquantificationset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    dataUrl = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    info = Column(Text)
    name = Column(Text, nullable=False)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)

    dataset = relationship('Dataset')
    referenceset = relationship('Referenceset')


class Sample(Base):
    __tablename__ = 'sample'
    __table_args__ = (
        Index('sample_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    diagnosisId = Column(Text)
    diagnosisIdTier = Column(Integer)
    localBiobankId = Column(Text)
    localBiobankIdTier = Column(Integer)
    collectionDate = Column(Text)
    collectionDateTier = Column(Integer)
    collectionHospital = Column(Text)
    collectionHospitalTier = Column(Integer)
    sampleType = Column(Text)
    sampleTypeTier = Column(Integer)
    tissueDiseaseState = Column(Text)
    tissueDiseaseStateTier = Column(Integer)
    anatomicSiteTheSampleObtainedFrom = Column(Text)
    anatomicSiteTheSampleObtainedFromTier = Column(Integer)
    cancerType = Column(Text)
    cancerTypeTier = Column(Integer)
    cancerSubtype = Column(Text)
    cancerSubtypeTier = Column(Integer)
    pathologyReportId = Column(Text)
    pathologyReportIdTier = Column(Integer)
    morphologicalCode = Column(Text)
    morphologicalCodeTier = Column(Integer)
    topologicalCode = Column(Text)
    topologicalCodeTier = Column(Integer)
    shippingDate = Column(Text)
    shippingDateTier = Column(Integer)
    receivedDate = Column(Text)
    receivedDateTier = Column(Integer)
    qualityControlPerformed = Column(Text)
    qualityControlPerformedTier = Column(Integer)
    estimatedTumorContent = Column(Text)
    estimatedTumorContentTier = Column(Integer)
    quantity = Column(Text)
    quantityTier = Column(Integer)
    units = Column(Text)
    unitsTier = Column(Integer)
    associatedBiobank = Column(Text)
    associatedBiobankTier = Column(Integer)
    otherBiobank = Column(Text)
    otherBiobankTier = Column(Integer)
    sopFollowed = Column(Text)
    sopFollowedTier = Column(Integer)
    ifNotExplainAnyDeviation = Column(Text)
    ifNotExplainAnyDeviationTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)
    startInterval = Column(Text)
    startIntervalTier = Column(Integer)

    dataset = relationship('Dataset')


class Sequencing(Base):
    __tablename__ = 'sequencing'
    __table_args__ = (
        Index('sequencing_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    sequencingId = Column(Text)
    sequencingIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    dnaLibraryKit = Column(Text)
    dnaLibraryKitTier = Column(Integer)
    dnaSeqPlatform = Column(Text)
    dnaSeqPlatformTier = Column(Integer)
    dnaReadLength = Column(Text)
    dnaReadLengthTier = Column(Integer)
    rnaLibraryKit = Column(Text)
    rnaLibraryKitTier = Column(Integer)
    rnaSeqPlatform = Column(Text)
    rnaSeqPlatformTier = Column(Integer)
    rnaReadLength = Column(Text)
    rnaReadLengthTier = Column(Integer)
    pcrCycles = Column(Text)
    pcrCyclesTier = Column(Integer)
    extractionId = Column(Text)
    extractionIdTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Slide(Base):
    __tablename__ = 'slide'
    __table_args__ = (
        Index('slide_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    slideId = Column(Text)
    slideIdTier = Column(Integer)
    slideOtherId = Column(Text)
    slideOtherIdTier = Column(Integer)
    lymphocyteInfiltrationPercent = Column(Text)
    lymphocyteInfiltrationPercentTier = Column(Integer)
    tumorNucleiPercent = Column(Text)
    tumorNucleiPercentTier = Column(Integer)
    monocyteInfiltrationPercent = Column(Text)
    monocyteInfiltrationPercentTier = Column(Integer)
    normalCellsPercent = Column(Text)
    normalCellsPercentTier = Column(Integer)
    tumorCellsPercent = Column(Text)
    tumorCellsPercentTier = Column(Integer)
    stromalCellsPercent = Column(Text)
    stromalCellsPercentTier = Column(Integer)
    eosinophilInfiltrationPercent = Column(Text)
    eosinophilInfiltrationPercentTier = Column(Integer)
    neutrophilInfiltrationPercent = Column(Text)
    neutrophilInfiltrationPercentTier = Column(Integer)
    granulocyteInfiltrationPercent = Column(Text)
    granulocyteInfiltrationPercentTier = Column(Integer)
    necrosisPercent = Column(Text)
    necrosisPercentTier = Column(Integer)
    inflammatoryInfiltrationPercent = Column(Text)
    inflammatoryInfiltrationPercentTier = Column(Integer)
    proliferatingCellsNumber = Column(Text)
    proliferatingCellsNumberTier = Column(Integer)
    sectionLocation = Column(Text)
    sectionLocationTier = Column(Integer)

    dataset = relationship('Dataset')


class Study(Base):
    __tablename__ = 'study'
    __table_args__ = (
        Index('study_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    endDate = Column(Text)
    endDateTier = Column(Integer)
    status = Column(Text)
    statusTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)

    dataset = relationship('Dataset')


class Surgery(Base):
    __tablename__ = 'surgery'
    __table_args__ = (
        Index('surgery_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    stopDate = Column(Text)
    stopDateTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    collectionTimePoint = Column(Text)
    collectionTimePointTier = Column(Integer)
    diagnosisDate = Column(Text)
    diagnosisDateTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)
    type = Column(Text)
    typeTier = Column(Integer)
    recordingDate = Column(Text)
    recordingDateTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)

    dataset = relationship('Dataset')


class Treatment(Base):
    __tablename__ = 'treatment'
    __table_args__ = (
        Index('treatment_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    courseNumber = Column(Text)
    courseNumberTier = Column(Integer)
    therapeuticModality = Column(Text)
    therapeuticModalityTier = Column(Integer)
    systematicTherapyAgentName = Column(Text)
    systematicTherapyAgentNameTier = Column(Integer)
    treatmentPlanType = Column(Text)
    treatmentPlanTypeTier = Column(Integer)
    treatmentIntent = Column(Text)
    treatmentIntentTier = Column(Integer)
    startDate = Column(Text)
    startDateTier = Column(Integer)
    stopDate = Column(Text)
    stopDateTier = Column(Integer)
    reasonForEndingTheTreatment = Column(Text)
    reasonForEndingTheTreatmentTier = Column(Integer)
    responseToTreatment = Column(Text)
    responseToTreatmentTier = Column(Integer)
    responseCriteriaUsed = Column(Text)
    responseCriteriaUsedTier = Column(Integer)
    dateOfRecurrenceOrProgressionAfterThisTreatment = Column(Text)
    dateOfRecurrenceOrProgressionAfterThisTreatmentTier = Column(Integer)
    unexpectedOrUnusualToxicityDuringTreatment = Column(Text)
    unexpectedOrUnusualToxicityDuringTreatmentTier = Column(Integer)
    drugIdNumbers = Column(Text)
    drugIdNumbersTier = Column(Integer)
    diagnosisId = Column(Text)
    diagnosisIdTier = Column(Integer)
    treatmentPlanId = Column(Text)
    treatmentPlanIdTier = Column(Integer)

    dataset = relationship('Dataset')


class Tumourboard(Base):
    __tablename__ = 'tumourboard'
    __table_args__ = (
        Index('tumourboard_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    patientId = Column(Text)
    patientIdTier = Column(Integer)
    dateOfMolecularTumorBoard = Column(Text)
    dateOfMolecularTumorBoardTier = Column(Integer)
    typeOfSampleAnalyzed = Column(Text)
    typeOfSampleAnalyzedTier = Column(Integer)
    typeOfTumourSampleAnalyzed = Column(Text)
    typeOfTumourSampleAnalyzedTier = Column(Integer)
    analysesDiscussed = Column(Text)
    analysesDiscussedTier = Column(Integer)
    somaticSampleType = Column(Text)
    somaticSampleTypeTier = Column(Integer)
    normalExpressionComparator = Column(Text)
    normalExpressionComparatorTier = Column(Integer)
    diseaseExpressionComparator = Column(Text)
    diseaseExpressionComparatorTier = Column(Integer)
    hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancer = Column(Text)
    hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancerTier = Column(Integer)
    actionableTargetFound = Column(Text)
    actionableTargetFoundTier = Column(Integer)
    molecularTumorBoardRecommendation = Column(Text)
    molecularTumorBoardRecommendationTier = Column(Integer)
    germlineDnaSampleId = Column(Text)
    germlineDnaSampleIdTier = Column(Integer)
    tumorDnaSampleId = Column(Text)
    tumorDnaSampleIdTier = Column(Integer)
    tumorRnaSampleId = Column(Text)
    tumorRnaSampleIdTier = Column(Integer)
    germlineSnvDiscussed = Column(Text)
    germlineSnvDiscussedTier = Column(Integer)
    somaticSnvDiscussed = Column(Text)
    somaticSnvDiscussedTier = Column(Integer)
    cnvsDiscussed = Column(Text)
    cnvsDiscussedTier = Column(Integer)
    structuralVariantDiscussed = Column(Text)
    structuralVariantDiscussedTier = Column(Integer)
    classificationOfVariants = Column(Text)
    classificationOfVariantsTier = Column(Integer)
    clinicalValidationProgress = Column(Text)
    clinicalValidationProgressTier = Column(Integer)
    typeOfValidation = Column(Text)
    typeOfValidationTier = Column(Integer)
    agentOrDrugClass = Column(Text)
    agentOrDrugClassTier = Column(Integer)
    levelOfEvidenceForExpressionTargetAgentMatch = Column(Text)
    levelOfEvidenceForExpressionTargetAgentMatchTier = Column(Integer)
    didTreatmentPlanChangeBasedOnProfilingResult = Column(Text)
    didTreatmentPlanChangeBasedOnProfilingResultTier = Column(Integer)
    howTreatmentHasAlteredBasedOnProfiling = Column(Text)
    howTreatmentHasAlteredBasedOnProfilingTier = Column(Integer)
    reasonTreatmentPlanDidNotChangeBasedOnProfiling = Column(Text)
    reasonTreatmentPlanDidNotChangeBasedOnProfilingTier = Column(Integer)
    detailsOfTreatmentPlanImpact = Column(Text)
    detailsOfTreatmentPlanImpactTier = Column(Integer)
    patientOrFamilyInformedOfGermlineVariant = Column(Text)
    patientOrFamilyInformedOfGermlineVariantTier = Column(Integer)
    patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfiling = Column(Text)
    patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfilingTier = Column(Integer)
    summaryReport = Column(Text)
    summaryReportTier = Column(Integer)
    actionableExpressionOutlier = Column(Text)
    actionableExpressionOutlierTier = Column(Integer)
    actionableGermlineVariant = Column(Text)
    actionableGermlineVariantTier = Column(Integer)
    germlineVariantsDrug = Column(Text)
    germlineVariantsDrugTier = Column(Integer)
    germlineVariantsDrugClass = Column(Text)
    germlineVariantsDrugClassTier = Column(Integer)
    germlineVariantsDiscussed = Column(Text)
    germlineVariantsDiscussedTier = Column(Integer)
    actionableSomaticVariants = Column(Text)
    actionableSomaticVariantsTier = Column(Integer)
    somaticVariantsDrug = Column(Text)
    somaticVariantsDrugTier = Column(Integer)
    somaticVariantsDrugClass = Column(Text)
    somaticVariantsDrugClassTier = Column(Integer)
    somaticVariantsDiscussed = Column(Text)
    somaticVariantsDiscussedTier = Column(Integer)
    anyActionableExpressionOutlier = Column(Text)
    anyActionableExpressionOutlierTier = Column(Integer)
    expressionDrug = Column(Text)
    expressionDrugTier = Column(Integer)
    expressionDrugClass = Column(Text)
    expressionDrugClassTier = Column(Integer)
    expressionTypeOfAnalysisUsed = Column(Text)
    expressionTypeOfAnalysisUsedTier = Column(Integer)
    expressionTypeOfInformationUtility = Column(Text)
    expressionTypeOfInformationUtilityTier = Column(Integer)
    expressionAlteredGene = Column(Text)
    expressionAlteredGeneTier = Column(Integer)
    expressionNonActionableGene = Column(Text)
    expressionNonActionableGeneTier = Column(Integer)
    expressionTypeOfAlteration = Column(Text)
    expressionTypeOfAlterationTier = Column(Integer)
    anyActionableGermlineVariants = Column(Text)
    anyActionableGermlineVariantsTier = Column(Integer)
    germlineVariantsTypeOfAnalysisUsed = Column(Text)
    germlineVariantsTypeOfAnalysisUsedTier = Column(Integer)
    germlineVariantsClassificationOfVariants = Column(Text)
    germlineVariantsClassificationOfVariantsTier = Column(Integer)
    germlineVariantsTypeOfInformationUtility = Column(Text)
    germlineVariantsTypeOfInformationUtilityTier = Column(Integer)
    anyActionableSomaticVariants = Column(Text)
    anyActionableSomaticVariantsTier = Column(Integer)
    somaticVariantsTypeOfAnalysisUsed = Column(Text)
    somaticVariantsTypeOfAnalysisUsedTier = Column(Integer)
    somaticVariantsTypeOfInformationUtility = Column(Text)
    somaticVariantsTypeOfInformationUtilityTier = Column(Integer)
    somaticVariantsNonActionable = Column(Text)
    somaticVariantsNonActionableTier = Column(Integer)

    dataset = relationship('Dataset')


class Variantcalling(Base):
    __tablename__ = 'variantcalling'
    __table_args__ = (
        Index('variantcalling_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    created = Column(Text, nullable=False)
    updated = Column(Text)
    name = Column(Text)
    description = Column(Text)
    variantCallingId = Column(Text)
    variantCallingIdTier = Column(Integer)
    sampleId = Column(Text)
    sampleIdTier = Column(Integer)
    inHousePipeline = Column(Text)
    inHousePipelineTier = Column(Integer)
    variantCaller = Column(Text)
    variantCallerTier = Column(Integer)
    tabulate = Column(Text)
    tabulateTier = Column(Integer)
    annotation = Column(Text)
    annotationTier = Column(Integer)
    mergeTool = Column(Text)
    mergeToolTier = Column(Integer)
    rdaToTab = Column(Text)
    rdaToTabTier = Column(Integer)
    delly = Column(Text)
    dellyTier = Column(Integer)
    postFilter = Column(Text)
    postFilterTier = Column(Integer)
    clipFilter = Column(Text)
    clipFilterTier = Column(Integer)
    cosmic = Column(Text)
    cosmicTier = Column(Integer)
    dbSnp = Column(Text)
    dbSnpTier = Column(Integer)
    alignmentId = Column(Text)
    alignmentIdTier = Column(Integer)
    site = Column(Text)
    siteTier = Column(Integer)

    dataset = relationship('Dataset')


class Variantset(Base):
    __tablename__ = 'variantset'
    __table_args__ = (
        Index('variantset_datasetId_name', 'datasetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    created = Column(Text)
    dataUrlIndexMap = Column(Text, nullable=False)
    datasetId = Column(ForeignKey('dataset.id'), nullable=False, index=True)
    metadata_ = Column('metadata', Text)
    name = Column(Text, nullable=False)
    referenceSetId = Column(ForeignKey('referenceset.id'), nullable=False, index=True)
    updated = Column(Text)
    patientId = Column(Text, nullable=False)
    sampleId = Column(Text, nullable=False)

    dataset = relationship('Dataset')
    referenceset = relationship('Referenceset')


class Callset(Base):
    __tablename__ = 'callset'
    __table_args__ = (
        Index('callset_variantSetId_name', 'variantSetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    biosampleId = Column(Text)
    name = Column(Text, nullable=False)
    variantSetId = Column(ForeignKey('variantset.id'), nullable=False, index=True)

    variantset = relationship('Variantset')


class Readgroup(Base):
    __tablename__ = 'readgroup'
    __table_args__ = (
        Index('readgroup_readGroupSetId_name', 'readGroupSetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    biosampleId = Column(Text)
    created = Column(Text)
    description = Column(Text)
    experiment = Column(Text)
    name = Column(Text, nullable=False)
    predictedInsertSize = Column(Integer)
    readGroupSetId = Column(ForeignKey('readgroupset.id'), nullable=False, index=True)
    sampleName = Column(Text)
    stats = Column(Text, nullable=False)
    updated = Column(Text)

    readgroupset = relationship('Readgroupset')


class Variantannotationset(Base):
    __tablename__ = 'variantannotationset'
    __table_args__ = (
        Index('variantannotationset_variantSetId_name', 'variantSetId', 'name', unique=True),
    )

    id = Column(Text, primary_key=True)
    attributes = Column(Text)
    analysis = Column(Text)
    annotationType = Column(Text)
    created = Column(Text)
    name = Column(Text, nullable=False)
    ontologyId = Column(ForeignKey('ontology.id'), nullable=False, index=True)
    updated = Column(Text)
    variantSetId = Column(ForeignKey('variantset.id'), nullable=False, index=True)

    ontology = relationship('Ontology')
    variantset = relationship('Variantset')
