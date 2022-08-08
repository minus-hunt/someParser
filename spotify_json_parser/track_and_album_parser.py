import json


def extract_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        templates = json.load(file)

    return templates


def track_and_album_save(templates, data_type):
    if data_type == 'track':
        with open(f'{data_type}_lib.txt', 'w', encoding='utf-8') as file:
            for track in templates['tracks']:
                track_name = track['track']
                artist_name = track['artist']
                file.write('--> ' + artist_name + ' - ' + track_name + '\n')
    elif data_type == 'album':
        with open(f'{data_type}_lib.txt', 'w', encoding='utf-8') as file:
            for track in templates['albums']:
                album_name = track['album']
                artist_name = track['artist']
                file.write('--> ' + artist_name + ' - ' + album_name + '\n')
    else:
        print('[Unknown data type!]')


def main():
    templates = extract_json_data('YourLibrary.json')

    track_and_album_save(templates, data_type='track')
    track_and_album_save(templates, data_type='album')


if __name__ == "__main__":
    main()
