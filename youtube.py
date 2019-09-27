from config import config
import requests

base_url = "https://www.googleapis.com/youtube/v3"
key = config['api_key']
channel = config['channel_id']
empty_data = {
    'name': 'null',
    'subs': 194,
    'views': 4875,
    'videos': 90
}


def get_subs_and_views():
    global base_url, key, channel, empty_data

    return empty_data

    params = {
        'part': 'id,statistics,snippet',
        'key': key,
        'id': channel
    }

    r = requests.get(url=f"{base_url}/channels", params=params)
    data = r.json()

    if data['pageInfo']['totalResults'] == 0:
        return empty_data

    stats = data['items'][0]['statistics']
    title = data['items'][0]['snippet']['title']

    return {
        'name': title,
        'subs': stats['subscriberCount'],
        'views': stats['viewCount'],
        'videos': stats['videoCount'],
    }
