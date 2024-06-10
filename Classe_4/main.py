import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob
import pandas as pd

api_client_id = ""  
api_client_secret = "" 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

playlist_list = ["2wWa7oTaziKa9FEKQ12aSs", "4zkB78CbXiSLdrs5SzK8yZ", "6Xw9RWUaUzw71gESwqIZ8X"]
offset = 0

def get_playlist(playlist, offset):
    resposta = spotify.playlist_items(playlist, offset=offset)
    with open(f'{playlist}-{offset}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    if resposta["next"] is None:
        print("Final")
        pass
    else:
        offset += 100
        print("Nova petició")
        get_playlist(playlist, offset)

for playlist in playlist_list:
    offset = 0
    get_playlist(playlist, offset)

files = glob.glob("*.json")
list_tracks = []

for file in files:
    with open(file) as f:
        d = json.load(f)
        print(d)
        tracks = d["items"]
        for track in tracks:
            track_dict = {
                "name": track["track"]["name"],
                "popularity": track["track"]["popularity"],
                "artist_name": track["track"]["artists"][0]["name"],
                "duracio_min": round(track["track"]["duration_ms"] / 1000 / 60, 2)
            }
            list_tracks.append(track_dict)

df = pd.DataFrame.from_dict(list_tracks)
df.to_csv("output.csv", index=False, sep=";")
