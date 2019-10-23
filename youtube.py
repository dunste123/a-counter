#                 GLWT(Good Luck With That) Public License
#                   Copyright (c) Everyone, except Author
#
#  Everyone is permitted to copy, distribute, modify, merge, sell, publish,
#  sublicense or whatever they want with this software but at their OWN RISK.
#
#                              Preamble
#
#  The author has absolutely no clue what the code in this project does.
#  It might just work or not, there is no third option.
#
#
#                  GOOD LUCK WITH THAT PUBLIC LICENSE
#     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION
#
#    0. You just DO WHATEVER YOU WANT TO as long as you NEVER LEAVE A
#  TRACE TO TRACK THE AUTHOR of the original product to blame for or hold
#  responsible.
#
#  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#
#  Good luck and Godspeed.
#
#  Everyone is permitted to copy, distribute, modify, merge, sell, publish,
#  sublicense or whatever they want with this software but at their OWN RISK.
#
#                              Preamble
#
#  The author has absolutely no clue what the code in this project does.
#  It might just work or not, there is no third option.
#
#
#                  GOOD LUCK WITH THAT PUBLIC LICENSE
#     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION
#
#    0. You just DO WHATEVER YOU WANT TO as long as you NEVER LEAVE A
#  TRACE TO TRACK THE AUTHOR of the original product to blame for or hold
#  responsible.
#
#  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#
#  Good luck and Godspeed.

from config import config
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

    if hasattr(data, 'error'):
        return default

    if data['pageInfo']['totalResults'] == 0:
        return default

    return data


def get_subs_and_views():
    return empty_data

    print('fetching new data')

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


def get_latest_video_id():
    return default_video_id

    print('fetching new video')

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
