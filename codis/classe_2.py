import spotipy       #CTRL+L limpiar consola // flecha arriba para última línea
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd    #pip install pandas (terminal)

api_client_id = "" #de la dashboard de iniciar sesión en Spotify for Developers
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_inicial = "7ltDVBr6mKbRvohxheJ9h1" #de la URL de Spotify Web Player (la URL del arista)
resposta = spotify.artist_related_artists(artist_inicial)
print(resposta)

artistes = resposta["artists"] #para acceder a la lista de artistas del archivo JSON

llista_artistes = []
for a in artistes: #para sacar del JSON la lista de artistas relacionados
    name = a['name']
    seguidores= a ['followers']['total'] #accede a la clave Total dentro de Followers dentro de "a"
    link = a['external_urls']['spotify']
    id= a['id']

    frame = pd.DataFrame({
        "semilla": artist_inicial,
        "name": name,
        "id": id,
        "seguidores": seguidores,
        "link": link,
    }, index=[0])
    llista_artistes.append(frame)

final = pd.concat(llista_artistes)
print(final)
final.to_excel("dataset.xlsx")
