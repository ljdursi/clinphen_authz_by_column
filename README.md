# ClinPhen column-level authorization PoC

Based on the CanDIG v1 data model, its [mock data](https://github.com/CanDIG/mock-data-generator), and realistic-ish access levels

## Installation

The server software can be installed in a virtual environment:

```
virtualenv -p python3 columnauthz
source columnauthz/bin/activate
pip install -r requirements.txt
python setup.py develop
```

### Running

The server can be run with, for instance

```
python3 -m clinphen_service
```

and you can compare the results to the contents of data/registry.db.  Results are mocked up as coming back from OPA (will try to do that next).  The idea is
that OPA would return the columns allowed for a given request, by dataset.  The user is supposed to have level 1 access to mock1 patients, enrollments, and level 3 to mock 2; and no access to biosamples information.  So for instance querying the patients resource, the column authorizations coming back would be:

```json
{
    "mock1": ["id", "patientId", "attributes", "datasetId", "created", "updated", "name", "description", "provinceOfResidence"],
    "mock2": ["id", "patientId", "attributes", "datasetId", "created", "updated", "name", "description", "dateOfBirth", "ethnicity", "race", "provinceOfResidence"]
}
```

(for simpliclity, not all columns are included).  

You can play with the API as so:

```bash
curl http://localhost:3000/v1/patients/     # works - note that not all records include ethnicity, race, or DOB fields
curl http://localhost:3000/v1/biosamples/   # authorizaiton fails, no authorization granted to any biosamples 
curl http://localhost:3000/v1/patients/PATIENT_37990
curl http://localhost:3000/v1/patients/PATIENT_37990/enrollments/
curl -X POST -H 'Content-Type: application/json' -d '[{"field": "provinceOfResidence", "op": "=", "value": "Yukon"}]'  http://localhost:3000/v1/patients/
curl -X POST -H 'Content-Type: application/json' -d '[{"field": "provinceOfResidence", "op": "=", "value": "Yukon"}, {"field": "dateOfBirth", "op": "=", "value": "1927-12-14"}]'  http://localhost:3000/v1/patients/ # note - filter will only succeed on mock2 records
```