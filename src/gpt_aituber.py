import requests
import os
from dotenv import load_dotenv
import json
from pathlib import Path

# meboAPIの使用
def miibo(MIIBO_API_KEY, MIIBO_AGENT_ID, prompt_input, max_tokens=300):
    load_dotenv()
    url = "https://api-mebo.dev/api"
    headers = {'content-type': 'application/json'}
    item_data = {
        "api_key": MIIBO_API_KEY,
        "agent_id": MIIBO_AGENT_ID,
        "utterance": prompt_input,
        "uid": "b3874853-ee47-cc4e-9ad2-f0e1c8806041"
    }
    response = requests.post(url,json=item_data,headers=headers)

    return response

def main(prompt):
    # これがないと.envの値が読み込まれない
    load_dotenv()
    # 環境変数からMIIBO_API_KEYとMIIBO_AGENT_IDを取得
    MIIBO_API_KEY = os.getenv("MIIBO_API_KEY")
    MIIBO_AGENT_ID = os.getenv("MIIBO_AGENT_ID")
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    aitube_output_path = Path(os.path.join(base_dir, '../output_test/aitube_output.txt'))
    response_path = Path(os.path.join(base_dir, '../output/response.json'))

    response = miibo(MIIBO_API_KEY, MIIBO_AGENT_ID, prompt)
    
    try:
        listener_text = response.json()["utterance"]
    except json.JSONDecodeError:
        print("Invalid JSON received.")
        print("Response content:", response.content)
    response_text = response.json()["bestResponse"]["utterance"]
    with open(aitube_output_path, mode="a", encoding='utf-8') as f:
        f.write(f'{listener_text}\n')
        f.write(f'{response_text}\n')

    response_output = {
        'listener': listener_text,
        'response': response_text
    }
    with open(response_path, 'w') as f:
        json.dump(response_output, f, indent=4)

    print("finish gpt_aituber.py")

# if __name__ == "__main__":
#     prompt = "僕はマカロニえんぴつの「レモンパイ」が好きだよ！ぬっこちゃんはマカロニえんぴつの何の曲が好き？"
#     main(prompt)