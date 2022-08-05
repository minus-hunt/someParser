import json

with open('Playlist1.json', encoding='utf-8') as file:
    templates = json.load(file)

playlists = templates['playlists']

for playlist in playlists:
     print(playlist['name'])
     for track in playlist['items']:
         print(track['track']['artistName'] + ' - ' + track['track']['trackName'] + '\n')
     print('\n')