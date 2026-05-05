import requests
import json

# Get pokemon API
pokemon_requests = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# Convert my data into Json format for readability

json_data = pokemon_requests.json()

# Cleaning my data 
# Creating a function to just show the name of each key attribute for a pokemon

def get_pokemon(data):
    return {
        "name": data["name"],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "types":[t["type"]["name"] for t in data["types"]],
        "stats":[s["stat"]["name"] for s in data["stats"]]
    }

print(get_pokemon(json_data))

clean_pokemon_data = get_pokemon(json_data)

# Saving and creating to a jsonfile

def save_to_new_json_file(data,filename):
    try:
        with open(filename, "w") as jsonfile:
            json.dump(data, jsonfile)
    except TypeError: #some types in python are not present in Jsonfiles 
        print("Type error")
    except Exception: #for all errors
        print("Unexpected error")

save_to_new_json_file(clean_pokemon_data, "pokemons_json_file.json")

# Checking if my file has been created function
import os

def check_if_file_created (file_name):
    try:
        os.path.exists(file_name)
        if os.path.exists(file_name)== True:
            return ("Yes, the file has been saved")
    except FileNotFoundError: # File can't be found error
        return ("File has not been saved")


print(check_if_file_created("pokemons_json_file.json"))

#Adding another Pokemon character (charizard)
pokemon_requests = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

print(pokemon_requests.content)

charizard_json_data = pokemon_requests.json()

def get_pokemon(data):
    return {
        "name": data["name"],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "types":[t["type"]["name"] for t in data["types"]],
        "stats":[s["stat"]["name"] for s in data["stats"]]
    }

print(get_pokemon(charizard_json_data))

# Adding and appending my json file function

def adding_pokemon_data(new_data, filename):
    if os.path.exists(filename): # If file exists
        with open(filename, "r") as file: # Open and read it
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError: # Handle if json file has errors 
                existing_data = []
        
    else:
        existing_data = [] # If we have nothing in our json file create an empty list

    if not isinstance(existing_data, list):
        existing_data = [existing_data] # Take whatever existing data is and wrap it in a list
    
    existing_data.append(new_data)

    save_to_new_json_file(existing_data, filename)

# Using my adding function for the charizard data

charizard_data = get_pokemon(charizard_json_data)

adding_pokemon_data(charizard_data, "pokemons_json_file.json")