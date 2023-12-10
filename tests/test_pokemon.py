import requests
import pytest

api = 'https://api.pokemonbattle.me:9104'

headers = {
    "Content-Type": "application/json",
    "trainer_token": "7ee5981a830b04546aac9b4c699550a1"
}

def test_get_trainers() :
    response = requests.get(api + '/trainers')
    assert response.status_code == 200
    
def test_trainer_name() :
    response = requests.get(api + '/trainers?trainer_id=3844')
    assert response.json()['trainer_name'] == 'DaryZay'