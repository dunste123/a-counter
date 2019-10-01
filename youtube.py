from config import config
import traceback
import requests

base_url = 'https://www.googleapis.com/youtube/v3'
key = config['api_key']
channel = config['channel_id']
empty_data = {
    'name': 'Donald Trump',
    'subs': -1,
    'views': -1,
    'videos': -1
}
default_video_id = 'dQw4w9WgXcQ'


def get_subs_and_views():
    # return empty_data

    print('fetching new data')

    try:
        params = {
            'part': 'id,statistics,snippet',
            'key': key,
            'id': channel
        }

        r = requests.get(url=base_url + '/channels', params=params)
        data = r.json()

        if data['error'] is not None:
            return empty_data

        if data['pageInfo']['totalResults'] == 0:
            return empty_data

        stats = data['items'][0]['statistics']
        title = data['items'][0]['snippet']['title']

        results = {
            'name': title,
            'subs': stats['subscriberCount'],
            'views': stats['viewCount'],
            'videos': stats['videoCount'],
        }

        print(results)

        return results
    except Exception:
        traceback.print_exc()
        return empty_data


def get_latest_video_id():
    # return default_video_id

    print('fetching new video')

    try:
        params = {
            'part': 'id,snippet',
            'key': key,
            'channelId': channel,
            'order': 'date'
        }

        r = requests.get(url=base_url + '/search', params=params)
        data = r.json()

        if data['error'] is not None:
            return default_video_id

        if data['pageInfo']['totalResults'] == 0:
            return default_video_id

        for item in data['items']:
            if item['id']['kind'] == 'youtube#video':
                print('new video id: ' + item['id']['videoId'])
                return item['id']['videoId']
    except Exception:
        traceback.print_exc()
        return default_video_id
