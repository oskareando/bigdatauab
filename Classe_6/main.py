####################
# pip install beautifulsoup4 #
# pip install requests #
# pip install spotipy #
# pip install lxml #
# pip install beautifulsoup4 #
# pip install openpyxl #
#############################################

import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time
import glob
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = ""  
SPOTIPY_CLIENT_SECRET = "" 

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# això defineix el rang d'anys a processar
rango = range(2000, 2024, 1)
for r in rango:
    print(r)

def extract_wiki(rango):
    for r in rango:
        try:
            resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{r}")
            codi_web = resposta.text  # s'obté el codi de la pàgina web

            soup = BeautifulSoup(codi_web, 'html.parser')
            final = soup.find('span', id="Final")  
            tabla = final.find_next("table") 
            df = pd.read_html(str(tabla))[0]

            print(df)
            df.to_excel(f"final-{r}.xlsx", index=False)  # es guarda el DataFrame en un fitxer Excel
            print(f"Tot correcte en {r}")
            time.sleep(1)
        except AttributeError:
            print(f"Problema en {r}")

def juntar():
    files = glob.glob("*.xlsx")
    print(files)

    llista_dfs = []
    for f in files:
        df = pd.read_excel(f)
        any = f.split("-")[1].split(".")[0]
        df["any"] = any
        df.columns.values[2] = "cantant"
        df.columns.values[5] = "punts"
        df.columns.values[0] = "N."

        llista_dfs.append(df)

    final_df = pd.concat(llista_dfs)
    final_df.to_excel("final-final.xlsx", index=False)  # volem guardar el DataFrame final en un fitxer Excel
    print(final_df)

df = pd.read_excel("final-final.xlsx")
print(df)

# Es busquen cançons a Spotify i desar els resultats en un fitxer JSON
for index, row in df.iterrows():
    cantant = row["cantant"]
    song = row["Canción"]
    any = row["any"]
    q = f"{song} {cantant} Eurovision"
    print(q)
    resposta = sp.search(q, limit=10, offset=0, type='track', market=None)
    resposta["query"] = q

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    print("Fet!")
    time.sleep(15)
