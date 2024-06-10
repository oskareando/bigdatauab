# Importació de llibreries necessàries
import spotipy       # Llibreria per interactuar amb l'API de Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import json          # Llibreria per treballar amb JSON
import pandas as pd  # Llibreria per gestionar dataframes i exportar a Excel

api_client_id = ""  
api_client_secret = "  

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

# Especificació de l'artista inicial (Rosalía en aquest cas)
artist_inicial = "7ltDVBr6mKbRvohxheJ9h1" 

# Obtenir artistes relacionats amb l'artista inicial
resposta = spotify.artist_related_artists(artist_inicial)

# Accés a la llista d'artistes relacionats des de la resposta JSON
artistes = resposta["artists"]

# Inicialització d'una llista per emmagatzemar les dades dels artistes
llista_artistes = []

# Recorregut per cada artista en la llista d'artistes relacionats i extracció de la informació rellevant
for a in artistes:
    name = a["name"]  # Nom de l'artista
    seguidors = a["followers"]["total"]  # Nombre de seguidors de l'artista
    link = a["external_urls"]["spotify"]  # Enllaç a Spotify de l'artista
    id = a["id"]  # ID de l'artista

    # Creació del dataframe de pandas per a cada artista amb la informació extreta
    frame = pd.DataFrame({
        "semilla": artist_inicial,
        "name": name,
        "id": id,
        "seguidors": seguidors,
        "link": link,
    }, index=[0])

    # Adició de cada dataframe a la llista d'artistes
    llista_artistes.append(frame)

# Concatenació de tots els dataframes en un de sol
final = pd.concat(llista_artistes)
print(final)

# Guardar el dataset en un fitxer Excel
final.to_excel("dataset.xlsx", index=False)  # Afegim index=False per evitar afegir una columna d'index innecessària
print("ACABAT!")
