import pytest

from utils.apiutils import getAPIData, postAPIData
from utils.myconfigparser import getPetAPIURL

baseURI = getPetAPIURL()
petID = '198'


@pytest.fixture #Este decorador se utiliza para definir funciones que proporcionan datos o recursos necesarios para las pruebas.
def add_pet():
    url = baseURI
    payload = {"id": int(petID), "name": "Cutie", "status": "available"}
    resp = postAPIData(url,payload)
    pet_ID = resp.json()['id']
    print(pet_ID)
    yield pet_ID #"fixture de generador". Esto significa que el valor pet_ID será proporcionado a las pruebas que lo soliciten utilizando una sintaxis especial de pytest.


def test_getPetByID(add_pet):
    url = baseURI + "/" + str(petID)
    headers = {'Content-Type': 'application/json'}
    resp = getAPIData(url, headers)
    assert resp.json()
    assert (resp.status_code == 200)
