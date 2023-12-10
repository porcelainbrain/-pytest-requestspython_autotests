import requests

api = 'https://api.pokemonbattle.me:9104'

headers = {
    "Content-Type": "application/json",
    "trainer_token": "7ee5981a830b04546aac9b4c699550a1"
}

response1 = requests.post(
    api + '/pokemons',
    headers = headers,
    json = {
        "name": "Чупакабра",
    }
)

print(response1.json())

response2 = requests.put(
    api + '/pokemons',
    headers = headers,
    json = {
        "pokemon_id": response1.json()["id"],
        "name": "Чупакабра2",
    }
)

print(response2.json())

response3 = requests.post(
    api + '/trainers/add_pokeball',
    headers = headers,
    json = {
        "pokemon_id": response2.json()["id"],
    }
)

print(response3.json())