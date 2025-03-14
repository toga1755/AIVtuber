import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import os
from pathlib import Path

def main(text):
    # スクリプトのあるディレクトリを取得
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 絶対パスを生成
    emotion_path = Path(os.path.join(base_dir, '../output/emotion.txt'))

    # 事前学習済みの日本語感情分析モデルとそのトークナイザをロード
    model = AutoModelForSequenceClassification.from_pretrained('christian-phu/bert-finetuned-japanese-sentiment')
    tokenizer = AutoTokenizer.from_pretrained('christian-phu/bert-finetuned-japanese-sentiment', model_max_lentgh=512)

    # 感情分析のためのパイプラインを設定
    nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, truncation=True)

    # テキストに対して感情分析を実行
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt', max_length=512)
    outputs = model(**inputs)
    logits = outputs.logits

    # ロジットを確率に変換
    probabilities = torch.softmax(logits, dim=1)[0]

    # 最も高い確率の感情ラベルを取得
    sentiment_label = model.config.id2label[torch.argmax(probabilities).item()]

    print(f"Sentiment: {sentiment_label}")

    if (sentiment_label == 'positive'):  
        with open(emotion_path, mode="w", encoding='utf-8') as f:
            f.write('0\n')
    elif (sentiment_label == 'negative'):
        with open(emotion_path, mode="w", encoding='utf-8') as f:
            f.write('1\n')
