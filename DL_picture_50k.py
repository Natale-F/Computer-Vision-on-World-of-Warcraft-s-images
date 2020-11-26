# -*- coding: utf-8 -*-
"""

# What is this script used for?

The purpose of this script is to download more informations about the top 
50 000 EU players in World of Warcraft (best items level). The names and realms 
of these players have been download in a previous notebook and store in a csv 
file. 
In this script I use Web Scraping on the official World of Warcraft website
(https://worldofwarcraft.com/) in order to retrieve more information on these 
characters as well as download an image.


# How is it done?

Using requests and json for data recovery, joblib to speed up the download and
pickle to store some informations.

@author: FOATA Natale
"""

import requests
import json
import pandas as pd

from bs4 import BeautifulSoup as bs


def save_fig(name, realm, url, path):
    """
    This function save the image store in "url" in a "path" of the computer and 
    add the name/realm to this new jpg file.
    
    Parameters
    ----------
    name : string
           name of the character
    realm : string
            realm of the character
    url : string
          url of the image
    path : string
           the path to store the figure

    Returns
    -------
    None.
    
    Example
    -------
    
    >>> name = "grømiam"
    >>> realm = "ysondre"
    >>> url = "https://render-eu.worldofwarcraft.com/character/ysondre/86/86129238-main.jpg"
    >>> path = "Data/With_background/"
    >>> save_fig(name, realm, url, path)
    
    --> Store the picture and create a file "grømiam-ysondre.jpg" in the folder
    Data/With_background/
    """
    # Get in the url
    response = requests.get(url)
    # Update the path to store the image in the url
    path_picture = path + str(name) + "-" + str(realm) + ".jpg"
    # Store the image in path_picture
    with open(path_picture, "wb") as file:
        file.write(response.content)
        file.close()



def infoPerso(name, server):
    """
    This function retrieves information from a character's page and saves the 
    associated image in a folder.
    Informations are return in a dictionnary and image is store in :
        - "Data/With_background/" if there is a background
        - "Data/Without_background/" if there isn't a background.

    Parameters
    ----------
    name : string
           the name of the character
    server : string
             the realm of the character

    Returns
    -------
    dico_info : dict
                dictionnary with name, class, faction, gender, race & url
                of the character
                
                
    Example
    -------
    
    >>> infoPerso("grømiam", "ysondre")
    
    --> {'name': 'Grømiam', 'class': 'shaman', 'faction': 'horde', 
         'gender': 'MALE', 'race': 'tauren',
        'url_with_background': 'https://render-eu.worldofwarcraft.com/character/ysondre/86/86129238-main.jpg',
        'url_character': 'https://render-eu.worldofwarcraft.com/character/ysondre/86/86129238-main-raw.png'}
    """

    # Use the name and the serveur to requests the website
    response = requests.get("https://worldofwarcraft.com/fr-fr/character/eu/" + str(server) +"/" + str(name))
    # Prepare the soup to parse the html
    soup = bs(response.content, "html.parser")
    # Retrieves the part of the html containing the data
    nice = soup.find("div", class_="react-mount")
    # These data are store in json format so we need to load with the json library
    json_nice = json.loads(nice['data-initial-state'])
    # Informations are in this part of the json file
    data = json_nice["summary"]["character"]
    
    # this dictionnary will countain the informations of the character
    dico_info = {}
    # add the informations to the dictionnary
    dico_info["name"] = data["name"]
    dico_info["class"] = data["class"]["slug"]
    dico_info["faction"] = data["faction"]["slug"]
    dico_info["gender"] = data["gender"]["enum"]
    dico_info["race"] = data["race"]["slug"]
    
    # Character image with class background
    json_url_part = data["render"]
    url_with_background =  json_url_part["static"]["url"]
    dico_info["url_with_background"] = url_with_background
    save_fig(name, server, url_with_background, "Data/With_background/")
    
    # sometimes this key isn't in this part of the file so we need to test it
    if 'foreground' in json_url_part.keys():
        url_character = json_url_part['foreground']['url']
        dico_info["url_character"] = url_character
        save_fig(name, server, url_character, "Data/Without_background/")
        
    # return a dictionnary
    return dico_info



def good_realm(realm): 
    """
    This function transform realm from the DataFrame previously download in a 
    usable format by an usable url. Spaces between 2 words must by replace by
    "-".

    Parameters
    ----------
    realm : string
            realm with space

    Returns
    -------
    TYPE
        DESCRIPTION.
          
    Example
    -------
    
    >>> good_realm("Old realm")
    --> 'Old-realm'
    """
    # split the string realm
    realm_split = realm.split()
    
    # if the realm have more than 1 word then join it with "-"
    if len(realm_split) > 1:
        new_realm =  "-".join(realm_split)
    # else do nothing 
    else:
        new_realm = realm
    # return realm in usable form
    return new_realm

# Import the previously data with top 50 000 EU characters
df = pd.read_csv("Data/characters_informations.csv", sep=";", header=0, 
                  names=["Rank", "Character", "Guild", "Realm", "ItemsLvl"])

# Transform the realm into usable realm for those who need it
df["realm_ok"] = df["Realm"].apply(good_realm)


def take_info(i):
    """
    This function makes it possible to integrate the above "infoPerso" function 
    in a parallelisation of the process with just 1 input variable.
    We use the above DataFrame to retrieve the name and server of the character
    rank with rank i.    

    Parameters
    ----------
    i : int
        the rank of the character in the top

    Returns
    -------
    TYPE
        DESCRIPTION.
             
    Example
    -------
    
    >>> take_info(0)
    --> {'name': 'Nekroth',
         'class': 'death-knight',
         'faction': 'alliance',
         'gender': 'MALE',
         'race': 'human',
         'url_with_background': 'https://render-eu.worldofwarcraft.com/character/alleria/70/133444422-main.jpg'}

    """
    
    # Data recovery testing
    try: 
        # recovers the line
        row = df.iloc[i]
        # character's name in string format
        name = str(row["Character"]).lower()
        # realm's name
        server = str(row["realm_ok"]).lower()
        # return the above function output
        return infoPerso(name, server)
    # if there is a problem return ''    
    except:
        return ''
    
import time, pickle   
from joblib import Parallel, delayed   


# =============================================================================
# Retrieving information and images for the 50,000 top players
# =============================================================================

# Number of characters to scrape
N = df.shape[0]

# Mesure execution time
s = time.time()
# Parallelize Web Scraping
characters_informations = Parallel(n_jobs=-1)(delayed(take_info)(i) for i in range(N))

# print execution time (40216,7sec on my laptop)
print('Execution time: %.2f.' %(time.time() - s))

# Store the informations in a pickle file
with open('Data/pickle/top_50k_informations.pkl', 'wb') as save_file:
    pickle.dump(characters_informations, save_file, protocol=pickle.HIGHEST_PROTOCOL)