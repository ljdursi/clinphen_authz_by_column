"""
API Data Model definitions
From Swagger file, with python classes via Bravado
"""

import pkg_resources
import yaml
from bravado_core.spec import Spec

#
# Read in the API definition, and parse it with Bravado
#
_API_DEF = pkg_resources.resource_filename('clinphen_service',
                                           'api/swagger.yaml')
_SPEC_DICT = yaml.safe_load(open(_API_DEF, 'r'))

_BRAVADO_CONFIG = {
    'validate_requests': False,
    'validate_responses': False,
    'use_models': True,
    'validate_swagger_spec': False
}

_SWAGGER_SPEC = Spec.from_dict(_SPEC_DICT, config=_BRAVADO_CONFIG)

#
# Generate the Python models from the spec
#

BASEPATH = _SWAGGER_SPEC.flattened_spec['basePath']
Error = _SWAGGER_SPEC.definitions['Error']  # pylint:disable=invalid-name
Patient = _SWAGGER_SPEC.definitions['Patient']  # pylint:disable=invalid-name
Biosample = _SWAGGER_SPEC.definitions['Biosample']  # pylint:disable=invalid-name
Enrollment = _SWAGGER_SPEC.definitions['Enrollment']  # pylint:disable=invalid-name
