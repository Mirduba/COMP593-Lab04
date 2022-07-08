import requests

# Base url of pokemon
url = "https://pokeapi.co/api/v2/pokemon/"

def search_pokemon(poke_name):
    """
    Get pokemon information

    :param poke_name: Send pokemon name as parameter
    :returns: returns poke dict if response is 200. Else print error code and reason
    
    """
    poke_name = str(poke_name).strip().lower() # convert user input to string, clear trailing space, and lowercase
    search_url = url + poke_name # concat baseurl with user input pokemon name
    response_message = requests.get(search_url) # sends GET requests to the search_url
    if response_message.status_code == requests.codes.ok: # if status_code == 200
        poke_dict = response_message.json() # returns the pokemon in json format
        return poke_dict # returns the poke_dict
    else:
        print(f"Status code: {response_message.status_code}, Error reason {response_message.reason}") # print status code and reason if status_code != 200

