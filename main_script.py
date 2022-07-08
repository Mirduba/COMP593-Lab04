from poke_api import search_pokemon
from pastebin_api import post_new_paste
from sys import argv


def main():
    user_input = argv[1]  # Command line input
    poke_dict = search_pokemon(user_input) # call function from poke_api.py
    if poke_dict:
        pastebin_title = user_input.upper() # print the pastbin title in upper case
        pastebin_body = get_pastebin_body(poke_dict) # call pastebin body function with poke_dict 
        pastebin_url = post_new_paste(pastebin_title, pastebin_body, '2W') # call function from pastebin_api.py and expiration for 14 days.
        print(pastebin_url) # print pastebin_url for this pokemon


def get_pastebin_body(poke_dict):
    poke_list = [i['ability']['name'] for i in poke_dict['abilities']] # get the name of the ability
    pastebin_body = "- "
    pastebin_body += "\n- ".join(poke_list) # custom format to print list
    return pastebin_body # returns the custom format list
    

main()