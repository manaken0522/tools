# tools
## soundcloud
### playlist_copier.py
プレイリストをコピーします
```
usage: playlist_copier.py [-h] playlist_id new_playlist_name client_id token datadome_client_id

positional arguments:
  playlist_id         Playlist ID
  new_playlist_name   New playlist name
  client_id           "client_id" URL parameter
  token               "Authorization" header
  datadome_client_id  "X-Datadome-Clientid" header

options:
  -h, --help          show this help message and exit
```
### playlist_sorter.py
プレイリストを並び替えます
```
usage: playlist_sorter.py [-h] playlist_id client_id token datadome_client_id

positional arguments:
  playlist_id         Playlist ID
  client_id           "client_id" URL parameter
  token               "Authorization" header
  datadome_client_id  "X-Datadome-Clientid" header

options:
  -h, --help          show this help message and exit
```