# pylint: disable=invalid-name
# pylint: disable=C0301
"""
Implement endpoints of model service
"""
from clinphen_service import orm
from clinphen_service.orm import models
from clinphen_service.api.logging import apilog, logger
from clinphen_service.api.logging import structured_log as struct_log
from clinphen_service.api.models import Error
from clinphen_service.api.models import Patient as api_patient
from clinphen_service.api.models import Biosample as api_biosample
from clinphen_service.api.models import Enrollment as api_enrollment
from clinphen_service.orm.models import Patient as orm_patient
from clinphen_service.orm.models import Biosample as orm_biosample
from clinphen_service.orm.models import Enrollment as orm_enrollment


def fake_authz(endpoint):
    """
    Returns dictionary of authorized fields, by dataset
    :param endpoint: name of endpoint (table name)
    :return: dictionary of authorized fields, by dataset
    """

    all_patient_fields =  ["id", "patientId", "attributes", "datasetId", "created",
                           "updated", "name", "description", "dateOfBirth",
                           "ethnicity", "race", "provinceOfResidence"]
    all_biosample_fields = ["id", "attributes", "created", "updated",
                            "datasetId", "description", "disease", "name",
                            "individualAgeAtCollection", "datasetId"]
    all_enrollment_fields = ["id", "attributes", "datasetId", "created",
                             "name", "description", "patientId",
                             "enrollmentApprovalDate", "ageAtEnrollment",
                             "eligibilityCategory", "primaryOncologistName",
                             "referringPhysicianName",
                             "referringPhysicianContact",
                             "summaryOfIdRequest", "treatingCentreName",
                             "treatingCentreProvince"]
    restricted_patient_fields = list(set(all_patient_fields) -
                                     set(["ethnicity", "race", "dateOfBirth"]))
    restricted_biosample_fields = list(set(all_biosample_fields) -
                                       set(["individualAgeAtCollection"]))
    restricted_enrollment_fields = list(set(all_enrollment_fields) -
                                        set(["eligibilityCategory", "summaryOfIdRequest",
                                            "treatingCentreName", "enrollmentApprovalDate",
                                            "primaryOncologistName", "referringPhysicianContact",
                                            "referringPhysicianName"]))
    # alice can't see any biosamples
    alices_entitlements = {
        "patient": { 
            "mock1": restricted_patient_fields,
            "mock2": all_patient_fields
        },
        "enrollment": {
            "mock1": restricted_enrollment_fields,
            "mock2": all_enrollment_fields
        }
    }

    if not endpoint in alices_entitlements:
        return None

    return alices_entitlements[endpoint]


def _report_search_failed(typename, exception, **kwargs):
    """
    Generate standard log message + request error for error:
    Internal error performing search

    :param typename: name of type involved
    :param exception: exception thrown by ORM
    :param **kwargs: arbitrary keyword parameters
    :return: Connexion Error() type to return
    """
    report = typename + ' search failed'
    message = 'Internal error searching for '+typename+'s'
    logger().error(struct_log(action=report, exception=str(exception), **kwargs))
    return Error(message=message, code=500)


def _report_conversion_error(typename, exception, **kwargs):
    """
    Generate standard log message + request error for warning:
    Trying to POST an object that already exists

    :param typename: name of type involved
    :param exception: exception thrown by ORM
    :param **kwargs: arbitrary keyword parameters
    :return: Connexion Error() type to return
    """
    report = 'Could not convert '+typename+' to ORM model'
    message = typename + ': failed validation - could not convert to internal representation'
    logger().error(struct_log(action=report, exception=str(exception), **kwargs))
    return Error(message=message, code=400)


def _report_unauthorized_error(typename, **kwargs):
    """
    Generate standard log message + request error for warning:
    Trying to POST an object that already exists

    :param typename: name of type involved
    :param **kwargs: arbitrary keyword parameters
    :return: Connexion Error() type to return
    """
    report = 'No authorization to access '+typename+' objects'
    message = typename + ': failed authorization - could not access.'
    logger().error(struct_log(action=report, **kwargs))
    return Error(message=message, code=405)


@apilog
def list_items(orm_class, api_class, object_name):
    """
    Return all authorized item
    """
    db_session = orm.get_session()
    fields = fake_authz(object_name)

    if not fields:
        err = _report_unauthorized_error(object_name)
        return err, 405

    results = []
    try:
        for dataset, columns in fields.items():
            q = db_session.query(orm_class).filter(orm_class.dataset.has(name=dataset)).all()
            results = results + [api_class(**orm.dump(p, fields=columns)) for p in q]
    except orm.ORMException as e:
        err = _report_search_failed(object_name, exception=e)
        return err, 500

    return results, 200

@apilog
def get_item_by_id(item_id, orm_class, api_class, object_name):
    """
    Return single item
    """
    db_session = orm.get_session()
    fields = fake_authz(object_name)

    if not fields:
        err = _report_unauthorized_error(object_name)
        return err, 405

    authzed_datasets = fields.keys()

    results = []
    try:
        q = db_session.query(orm_class)
        for dataset in authzed_datasets:
            authzed = q.filter(orm_class.dataset.has(name=dataset)).filter(orm_class.id == item_id).one_or_none()
            if authzed:
                results.append(orm.dump(authzed, fields=fields[dataset]))
    except orm.ORMException as e:
        err = _report_search_failed(object_name, e, var_id=str(item_id))
        return err, 500

    if not results:
        err = Error(message=f"No {object_name} found: {item_id}", code=404)
        return err, 404

    return api_class(**results[0]), 200

@apilog
def get_patient_by_id(patient_id):
    """
    Return single patient.  This one is different because patientId != Patient.id (I know, I know)
    """
    db_session = orm.get_session()
    fields = fake_authz('patient')

    if not fields:
        err = _report_unauthorized_error('patient')
        return err, 405

    authzed_datasets = fields.keys()

    results = []
    try:
        q = db_session.query(orm_patient)
        for dataset in authzed_datasets:
            authzed = q.filter(orm_patient.dataset.has(name=dataset)).filter(orm_patient.patientId==patient_id).one_or_none()
            if authzed:
                results.append(orm.dump(authzed, fields=fields[dataset]))
    except orm.ORMException as e:
        err = _report_search_failed('patient', e, var_id=str(patient_id))
        return err, 500

    if not results:
        err = Error(message=f"No patient found: {patient_id}", code=404)
        return err, 404

    return api_patient(**results[0]), 200


@apilog
def get_related_items_by_patient_id(patient_id, orm_class, api_class, object_name):
    """
    Return items with a Patient relationship
    """
    db_session = orm.get_session()
    fields = fake_authz(object_name)

    if not fields:
        err = _report_unauthorized_error(object_name)
        return err, 405

    patient_or_error, code = get_patient_by_id(patient_id)
    if code != 200:
        return patient_or_error, code

    authzed_datasets = fields.keys()

    results = []
    try:
        q = db_session.query(orm_class)
        for dataset in authzed_datasets:
            authzed = q.filter(orm_class.dataset.has(name=dataset)).filter(orm_class.patientId==patient_id).all()
            if authzed:
                results = results + [api_class(**orm.dump(item, fields=fields[dataset])) for item in authzed]
    except orm.ORMException as e:
        err = _report_search_failed(object_name, e, patient_id=str(patient_id))
        return err, 500

    # it's not an error if there are no such linked objects
    return results, 200


@apilog
def get_biosamples():
    return list_items(orm_biosample, api_biosample, 'biosample')


@apilog
def get_one_biosample(biosample_id):
    return get_item_by_id(biosample_id, orm_biosample, api_biosample, 'biosample')


@apilog
def get_enrollments():
    return list_items(orm_enrollment, api_enrollment, 'enrollment')


@apilog
def get_one_enrollment(enrollment_id):
    return get_item_by_id(enrollment_id, orm_enrollment, api_enrollment, 'enrollment')


@apilog
def get_patients():
    return list_items(orm_patient, api_patient, 'patient')


@apilog
def get_one_patient(patient_id):
    return get_patient_by_id(patient_id)


@apilog
def get_biosamples_by_patient(patient_id):
    return get_related_items_by_patient_id(patient_id, orm_biosample, api_biosample, 'biosample')


@apilog
def get_enrollments_by_patient(patient_id):
    return get_related_items_by_patient_id(patient_id, orm_enrollment, api_enrollment, 'enrollment')


# def biosample_exists(id=None, chromosome=None,  # pylint:disable=redefined-builtin
#                    start=None, alt=None, ref=None, **_kwargs):
#     """
#     Check to see if biosample exists, by ID if given or if by features if not
#     """
#     if id is not None:
#         if Biosample().query.get(id).count() > 0:
#             return True
#     if Biosample().query.filter(models.Biosample.chromosome == chromosome)\
#         .filter(and_(models.Biosample.start == start,
#                      models.Biosample.alt == alt,
#                      models.Biosample.ref == ref)).count() > 0:
#         return True

#     return False


# def patient_exists(db_session, id=None, description=None, **_kwargs):  # pylint:disable=redefined-builtin
#     """
#     Check to see if patient exists, by ID if given or if by features if not
#     """
#     if id is not None:
#         return db_session.query(models.Patient)\
#                           .filter(models.Patient.id == id).count() > 0

#     if description is not None:
#         return db_session.query(models.Patient)\
#                           .filter(models.Patient.description == description).count() > 0

#     return False


@apilog
def get_patients_by_biosample(biosample_id):
    pass
#     """
#     Return biosamples that have been called in an patient
#     """
#     db_session = orm.get_session()

#     try:
#         var = db_session.query(orm.models.Biosample)\
#             .filter(orm.models.Biosample.id == biosample_id)\
#             .one_or_none()
#     except orm.ORMException as e:
#         err = _report_search_failed('biosample', e, biosample_id=biosample_id)
#         return err, 500

#     if not var:
#         err = Error(message="No biosample found: "+str(biosample_id), code=404)
#         return err, 404

#     try:
#         patients = [call.patient for call in var.calls
#                        if call.patient is not None]
#     except orm.ORMException as e:
#         err = _report_search_failed('patients', e, by_biosample_id=biosample_id)
#         return err, 500

#     return [orm.dump(i) for i in patients], 200
