from rich import print
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

#spotifyインスタンスを作成
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=config.CLIENT_ID,
	client_secret=config.CLIENT_SECRET,
    )
)

results = sp.search(q="BE:FIRST", limit=5, type="track")
for track in results["tracks"]["items"]:
    track_name = track["name"]
    # インラインで[]を使って色を指定
    print(f"[bold red]Track[/bold red]: {track_name} ")


# print("[red]Hello[/red] [italic cyan]World[/italic cyan]!")