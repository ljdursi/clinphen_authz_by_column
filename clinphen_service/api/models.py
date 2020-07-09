"""
API Data Model definitions
From Swagger file, with python classes via Bravado
"""

from marshmallow import Schema, fields

class Patient(Schema):
    id = fields.String()
    patientId = fields.String()
    attributes = fields.String()
    datasetId = fields.String()
    created = fields.String()
    updated = fields.String()
    name = fields.String()
    description = fields.String()
    dateOfBirth = fields.String()
    gender = fields.String()
    ethnicity = fields.String()
    race = fields.String()
    provinceOfResidence = fields.String()

class Biosample(Schema):
    id = fields.String()
    attributes = fields.String()
    created = fields.String()
    updated = fields.String()
    description = fields.String()
    disease = fields.String()
    name = fields.String()
    individualAgeAtCollection = fields.String()
    datasetId = fields.String()

class Error(Schema):
    code = fields.Integer()
    message = fields.String()

class Enrollment(Schema):
    id = fields.String()
    attributes = fields.String()
    datasetId = fields.String()
    created = fields.String()
    format = fields.String()
    updated = fields.String()
    name = fields.String()
    description = fields.String()
    patientId = fields.String()
    enrollmentApprovalDate = fields.String()
    ageAtEnrollment = fields.String()
    eligibilityCategory = fields.String()
    primaryOncologistName = fields.String()
    referringPhysicianName = fields.String()
    referringPhysicianContact = fields.String()
    summaryOfIdRequest = fields.String()
    treatingCentreName = fields.String()
    treatingCentreProvince = fields.String()