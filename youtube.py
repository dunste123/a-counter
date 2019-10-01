from config import config
import requests

base_url = 'https://www.googleapis.com/youtube/v3'
key = config['api_key']
channel = config['channel_id']
empty_data = {
    'name': 'Orange',
    'subs': 194,
    'views': 4875,
    'videos': 90
}
default_video_id = 'dQw4w9WgXcQ'


def get_subs_and_views():
    return empty_data

    try:
        params = {
            'part': 'id,statistics,snippet',
            'key': key,
            'id': channel
        }

        r = requests.get(url=base_url + '/channels', params=params)
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
    except:
        return empty_data


def get_latest_video_id():
    return default_video_id

    try:
        params = {
            'part': 'id,snippet',
            'key': key,
            'channelId': channel,
            'order': 'date'
        }

        r = requests.get(url=base_url + '/search', params=params)
        data = r.json()

        if data['pageInfo']['totalResults'] == 0:
            return empty_data

        for item in data['items']:
            if item['id']['kind'] == 'youtube#video':
                return item['id']['videoId']
    except:
        return default_video_id
