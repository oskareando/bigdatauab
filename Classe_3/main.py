import spotipy  # Llibreria per interactuar amb l'API de Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd  # Llibreria per gestionar dataframes i exportar a CSV

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

artist_id = "6k8mwkKJKKjBILo7ypBspl"  # ID de l'artista inicial (Ana Mena)

def get_related(artist_id):
    resposta = spotify.artist_related_artists(artist_id)
    return resposta

result = get_related(artist_id)

# Recollir dades d'artistes relacionats
llista_de_relacionats = []
for artist in result["artists"]:
    artista = {
        "origen": "ana mena",
        "desti": artist["name"],
        "generes": artist["genres"],
        "id": artist["id"]
    }
    llista_de_relacionats.append(artista)

llista_definitiva = []
for a in llista_de_relacionats:
    llista_definitiva.append(a)
    id = a["id"]
    result = get_related(id)
    for artist in result["artists"]:
        artista = {
            "origen": a["desti"],
            "desti": artist["name"],
            "generes": artist["genres"],
            "id": artist["id"]
        }
        llista_definitiva.append(artista)

# Crear tuples per a l'exportació
llista_tuples = []
for i in llista_definitiva:
    llista_tuples.append((i["origen"], i["desti"]))

for i in llista_definitiva:
    for g in i["generes"]:
        llista_tuples.append((i["origen"], g))

# Convertir a dataframe i exportar a CSV
df = pd.DataFrame(llista_tuples, columns=["source", "target"])
print(df)
df.to_csv("graf_generes.csv", sep=",", index=False)
