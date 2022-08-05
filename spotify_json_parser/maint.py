import json

def extract_data_from_json(file_path):
    '''Достаем данные'''
    with open(file_path, encoding='utf-8') as file:
        templates = json.load(file)

    # функция возвращает объект типа list
    return templates['playlists']


def write_tracks_in_txt(list_of_playlists):
    '''Записываем в текстовый файл'''
    with open("tracks_from_spotify.txt", 'w', encoding='utf-8') as file:
        for playlist in list_of_playlists:
            file.write(f'[{playlist["name"]}]' + '\n')
            for track in playlist['items']:
                artistName = track['track']['artistName']
                trackName = track['track']['trackName']
                file.write('---> ' + artistName + ' - ' + trackName + '\n')
            file.write('\n')


def main():
    list_of_playlists = extract_data_from_json('Playlist1.json')
    write_tracks_in_txt(list_of_playlists)


if __name__ == "__main__":
    main()