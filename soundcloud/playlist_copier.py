import argparse
import requests

def copy(args):
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
        tracks = [d.get('id') for d in tracks]
        print(tracks)
        response = requests.post(f"https://api-v2.soundcloud.com/playlists?client_id={args.client_id}&app_version={app_version}&app_locale=en", headers=headers, json={"playlist":{"title":args.new_playlist_name,"sharing":"public","tracks":tracks,"_resource_id":"f-27","_resource_type":"playlist"}})
        if response.status_code == 201:
            print(f"プレイリストのコピーが完了しました {response.json()['permalink_url']}")

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("playlist_id", help="Playlist ID")
    argparser.add_argument("new_playlist_name", help="New playlist name")
    argparser.add_argument("client_id", help="\"client_id\" URL parameter")
    argparser.add_argument("token", help="\"Authorization\" header")
    argparser.add_argument("datadome_client_id", help="\"X-Datadome-Clientid\" header")
    args = argparser.parse_args()
    copy(args)