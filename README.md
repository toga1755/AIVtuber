# AIVtuber

Git LFSを使用しているので、リポジトリのクローンを作成する際にGit LFSが必要になります。(by GitHubCopilot)

## クローン後の手順

リポジトリをクローンした後、以下のコマンドを実行してGit LFSのファイルを取得してください。

```bash
git lfs pull
```

## .envファイルについて

APIやらなんやらを取得しないといけない

### YOUTUBE_VIDEO_ID

これはyoutubeのlive配信の枠を立ててからじゃないと取得できない  
枠を立てたら配信ページに行って、v=より後の文字列(v=は含めない)をコピー

![YOUTUBE_VIDEO_ID](./素材/スクリーンショット%202025-03-15%20234337.png)

### YOUTUBE_DATA_API_KEY

これは事前に用意できる  
[この記事](https://qiita.com/shinkai_/items/10a400c25de270cb02e4)を参考に取得してね

### MIIBO

MIIBOはよく覚えてないけど、アカウント作ってエージェント作れば、IDをAPIがわかるはず