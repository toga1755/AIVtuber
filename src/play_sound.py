import tkinter as tk
import winsound
import wave
import contextlib
import os
from pathlib import Path

def get_wav_length(file_path):
    file_path = str(file_path)
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        # ミリ秒に変換、音声終了から1秒後にウィンドウを閉じる
        return duration * 1000 + 1000

def play_sound():
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    output_path = Path(os.path.join(base_dir, '../output/output.wav'))

    winsound.PlaySound(output_path, winsound.SND_FILENAME)

def main():
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    output_path = Path(os.path.join(base_dir, '../output/output.wav'))

    # WAVファイルの長さを取得
    wav_length = get_wav_length(output_path)

    # tkinter ウィンドウの作成
    window = tk.Tk()
    window.title("音声自動再生")

    # 起動後1秒で play_sound 関数を実行
    window.after(1000, play_sound)

    # WAVファイルの長さに基づいてウィンドウを閉じる
    window.after(int(wav_length), window.destroy)

    # ウィンドウの実行
    window.mainloop()

    print("finish play_sound.py")

if __name__ == "__main__":
    main()