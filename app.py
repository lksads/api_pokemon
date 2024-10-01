import requests

# URL base da PokeAPI
url = "https://pokeapi.co/api/v2/pokemon/"

# Função para obter informações de um Pokémon
def get_pokemon_info(pokemon_name):
    response = requests.get(url + pokemon_name)
    if response.status_code == 200:
        data = response.json()
        # Exibindo algumas informações do Pokémon
        print(f"Nome: {data['name']}")
        print(f"Altura: {data['height']} Mts")
        print(f"Peso: {data['weight']} Kg")
        print(f"Tipos: {[type_info['type']['name'] for type_info in data['types']]}")
    else:
        print(f"Erro ao buscar Pokémon: {response.status_code}")

# Nome do Pokémon que você quer buscar
pokemon = input("Digite o nome do Pokémon: ")
get_pokemon_info(pokemon)
