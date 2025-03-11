import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '366ecdf7680ffb070daf375620c7a702'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = 22730

def test_status_code():
    response = requests.get(url= f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Наум'

@pytest.mark.parametrize('key, value', [('trainer_name','Наум'),('id',f'{TRAINER_ID}')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url= f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value