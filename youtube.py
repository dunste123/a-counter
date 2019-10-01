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


def request_or_default(path, params, default=None):
    params['key'] = key
    r = requests.get(url=base_url + path, params=params)
    data = r.json()

    print(data)

    if data['error'] is not None:
        return default

    if data['pageInfo']['totalResults'] == 0:
        return default

    return data


def get_subs_and_views():
    # return empty_data

    print('fetching new data')

    try:
        params = {
            'part': 'id,statistics,snippet',
            'id': channel
        }

        data = request_or_default(path='/channels', params=params, default=empty_data)

        stats = data['items'][0]['statistics']
        title = data['items'][0]['snippet']['title']

        return {
            'name': title,
            'subs': stats['subscriberCount'],
            'views': stats['viewCount'],
            'videos': stats['videoCount'],
        }
    except:
        traceback.print_exc()
        return empty_data


def get_latest_video_id():
    # return default_video_id

    print('fetching new video')

    try:
        params = {
            'part': 'id,snippet',
            'channelId': channel,
            'order': 'date'
        }

        data = request_or_default(path='/search', params=params, default=default_video_id)

        for item in data['items']:
            if item['id']['kind'] == 'youtube#video':
                print('new video id: ' + item['id']['videoId'])
                return item['id']['videoId']
    except:
        traceback.print_exc()
        return default_video_id
