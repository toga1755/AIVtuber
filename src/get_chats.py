# 環境変数読み込み用ライブラリ
from dotenv import load_dotenv
import os
# URL読み込み用ライブラリ
import requests
import json
from pathlib import Path


def get_live_chat_id(youtube_video_id, youtube_data_api_key):
    params = {
        'part': 'liveStreamingDetails',
        'id': youtube_video_id,
        'key': youtube_data_api_key
    }
    response = requests.get(
        'https://youtube.googleapis.com/youtube/v3/videos', params=params)
    json_data = response.json()

    if len(json_data['items']) == 0:
        return ""

    live_chat_id = json_data['items'][0]['liveStreamingDetails']['activeLiveChatId']
    return live_chat_id

# ライブチャットのメッセージを取得


def get_live_chat_messages(live_chat_id, api_key):
    params = {
        'liveChatId': live_chat_id,
        'part': 'id,snippet,authorDetails',
        'maxResults': 200,  # 最大200まで指定可能
        'key': api_key
    }
    response = requests.get(
        'https://youtube.googleapis.com/youtube/v3/liveChat/messages', params=params)
    return response.json()


def main():
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    live_chat_messages_path = Path(os.path.join(base_dir, '../output/live_chat_messages.json'))

    # 環境変数読み込み
    load_dotenv()
    YOUTUBE_VIDEO_ID = os.getenv("YOUTUBE_VIDEO_ID")
    YOUTUBE_DATA_API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")

    video_id = YOUTUBE_VIDEO_ID
    api_key = YOUTUBE_DATA_API_KEY

    # ライブチャットIDを取得
    live_chat_id = get_live_chat_id(video_id, api_key)

    # ライブチャットのメッセージを取得
    live_chat_messages = get_live_chat_messages(live_chat_id, api_key)

    with open(live_chat_messages_path, 'w') as f:
        pass

    list_dict = []

    # 取得したメッセージを表示
    for i, message in enumerate(live_chat_messages.get('items', [])):
        # 辞書型に出力
        chats_dict = {
            'number': i,
            'author': message['authorDetails']['displayName'],
            'message': message['snippet']['displayMessage']
        }
        list_dict.append(chats_dict)

    # 取得したメッセージをjson形式で出力
    # メッセージを撤回すると、そのメッセージは取得できない。
    # つまり、数がずれる可能性がある。
    # とりあえず考えず取得するだけ
    with open(live_chat_messages_path, 'a') as f:
        json.dump(list_dict, f, indent=4)


if __name__ == "__main__":
    main()