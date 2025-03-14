import time
import json
import get_chats
import gpt_aituber
import output_voice
import play_sound
import emotional_analysis
import os

cnt_comment_before = 0

# スクリプトのあるディレクトリを取得
base_dir = os.path.dirname(os.path.abspath(__file__))
# ファイルへの絶対パスを生成
live_chat_messages_path = os.path.join(base_dir, '../output/live_chat_messages.json')
response_path = os.path.join(base_dir, '../output/response.json')
txt_message_path = os.path.join(base_dir, '../output/txt_message.txt')
txt_response_path = os.path.join(base_dir, '../output/txt_response.txt')

# 定期的にyoutubeコメントをチェックする
while True:

    # youtube
    get_chats.main()

    # json形式のファイルをデコードし、内容を変数に格納する
    with open(live_chat_messages_path) as f:
        d = json.load(f)

    # コメントが追加された場合
    if len(d) > cnt_comment_before:
        cnt_added = len(d) - cnt_comment_before
        print(f'{cnt_added} comment was added')

        cnt_comment_before = len(d)

        # 最新のコメントの内容を表示する
        print(f"ユーザー：{d[cnt_comment_before-1]['author']}")
        print(f"コメント：{d[cnt_comment_before-1]['message']}")
        message = d[cnt_comment_before-1]['message']

        # gptによる応答生成
        gpt_aituber.main(message)
        try:
            with open(response_path) as f:
                res = json.load(f)
        except json.JSONDecodeError:
            res = {'response': ''}
        print(res['response'])

        # 応答のポジティブネガティブ判定
        emotional_analysis.main(res['response'])
        
        # obs表示用のテキストデータを出力
        with open(txt_message_path, encoding='UTF-8', mode='w') as f:
            f.write(message)
        with open(txt_response_path, encoding='UTF-8', mode='w') as f:
            f.write(res['response'])

        # 音声データ出力
        output_voice.output_voice(res['response'])

        # 音声データ再生
        play_sound.main()


    # 5秒待機
    time.sleep(5)