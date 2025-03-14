from pprint import pprint
from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
import os

# VOICEVOXを用いて文字列をwavファイルに変換する
def output_voice(text_input):
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    dict_path = Path(os.path.join(base_dir, '../open_jtalk_dic_utf_8-1.11'))
    info_voice_path = Path(os.path.join(base_dir, '../output_test/info_voice.txt'))
    output_path = Path(os.path.join(base_dir, '../output/output.wav'))

    core = VoicevoxCore(open_jtalk_dict_dir=dict_path)

    # 音声モデルの一覧を出力
    with open(info_voice_path, 'w', encoding='utf-8') as f:
        pprint(METAS, stream=f)

    # ボイスの設定 詳細はinfo_voice.txtを参照
    speaker_id = 2

    if not core.is_model_loaded(speaker_id):
        core.load_model(speaker_id)
    wave_bytes = core.tts(text_input, speaker_id)

    # 音声ファイルに書き出す
    with open(output_path, "wb") as f:
        f.write(wave_bytes)

    print('finish output_voice.py')

# if __name__ == "__main__":
#     # テスト用
#     text_input = "私はぬっこちゃんです。よろしくお願いします。"
#     output_voice(text_input)