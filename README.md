# Pokemon Data Pipeline Project
For this project I built a simple data pipeline in Python that requests data from the public PokeAPI, transforms it, and loads the selected data into a structured JSON file. 

## Objectives of the Project
* To understand how rest APIs work and use them practically.
* Use python to make HTTP requests to the Pokemon API. 
* Process and extract relevant fields from the API response.
* Transform the data into a simplified structure. 
* Save the processed data into a JSON file.

## Technologies Used
*	Python 
*	Requests library
*	JSON
*	PokeAPI

## Setup Instructions
1. Install dependencies
   Pip install requests
   
2. Clone the repository
   Git clone <my-repo-url>
   cd pokemon-data-pipeline

## How To Run
1.	Make sure you have python installed.
2.	Navigate to the project folder: 
‘’’ bash 
Cd pokemon-data-pipeline
3.	Run the script:
Python pokemon_pipeline.py

# Example Output 
JSON 
[
  {
    "name": "pikachu",
    "abilities": [
      "static",
      "lightning-rod"
    ],
    "types": [
      "electric"
    ],
    "stats": [
      "hp",
      "attack",
      "defense",
      "special-attack",
      "special-defense",
      "speed"
    ]
  }
]

## Project Structure 
pokemon-data-pipeline/
│
├── pokemon_pipeline.py # Python pipeline script
├── pokemons_json_file.json # Output data file
└── README.md # Project documentation

## Pipeline Summary 
This data pipeline retrieves, processes, and stores Pokemon data. The pipeline begins by sending a request to the Pokemon API to fetch raw data for the given Pokemon name inserted in the endpoint by the user. The response is then converted into a Python dictionary and cleaned with functions that extract only relevant fields that we were interested in of the pokemon. These include “name”, “abilities”, “types, and “stats”. 

This data is now transformed into a simplified structure and saved into a JSON file using a json.dump function. If the file already exists, users can load the file and add new Pokemon data for different characters with the append function rather than overwriting existing entries. 

Pipeline workflow: extract -> transform -> store
