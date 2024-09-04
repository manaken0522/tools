import argparse
import requests

def sort_playlist(args):
    response = requests.get("https://soundcloud.com/versions.json")
    app_version = response.json()["app"]

    headers = {
        "Authorization": args.token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "X-Datadome-Clientid": args.datadome_client_id,
    }

    response = requests.get(f"https://api-v2.soundcloud.com/playlists/{args.playlist_id}?client_id={args.client_id}&app_version={app_version}&app_locale=en", headers=headers)
    if response.status_code == 200:
        tracks = response.json()["tracks"]
        sorted_tracks = [d.get('id') for d in sorted(tracks, key=lambda t:t["id"])]
        response = requests.put(f"https://api-v2.soundcloud.com/playlists/{args.playlist_id}?client_id={args.client_id}&app_version={app_version}&app_locale=en", headers=headers, json={"playlist":{"tracks":sorted_tracks}})
        if response.status_code == 200:
            print("プレイリストがソートされました")
            print(sorted_tracks)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("playlist_id", help="Playlist ID")
    argparser.add_argument("client_id", help="\"client_id\" URL parameter")
    argparser.add_argument("token", help="\"Authorization\" header")
    argparser.add_argument("datadome_client_id", help="\"X-Datadome-Clientid\" header")
    args = argparser.parse_args()
    sort_playlist(args)