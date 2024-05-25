import json

import pytest

from utils.apiutils import getAPIData, postAPIData
from utils.myconfigparser import getPetAPIURL

baseURI = getPetAPIURL()

testdata = [
    ('available', 200),
    ('pending', 200),
    ('sold', 200)
]


@pytest.mark.parametrize("type,status", testdata)  # Lo que vamos a hacer
# aqui es que se va a ser una prueba para cada estado
def test_getPetByStatus(type, status):
    url = baseURI + "/" + "findByStatus"
    params = {'status': type}
    resp = getAPIData(url, params=params)
    assert resp.status_code == status
    print(json.dumps(resp.json(), indent=3))
