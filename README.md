# YouTube動画ダウンロードスクリプト

YouTubeの動画をMP4形式でダウンロードするためのPythonスクリプトです。`yt-dlp` と `ffmpeg` を利用しています。

---

## 📄 前提条件

-   **Python 3.x** がインストールされていること
-   **yt-dlp** がインストールされていること
    ```bash
    pip install yt-dlp
    ```
-   **ffmpeg** がインストールされていること（スクリプトでパス指定可能）

---

## 🚀 使い方

### 基本コマンド

python yt2mp4_ytdlp.py "[https://www.youtube.com/watch?v=xxxx](https://www.youtube.com/watch?v=xxxx)"

引数 "https://www.youtube.com/watch?v=xxxx" はダウンロードしたいYouTube動画のURLに置き換えてください。

### オプション
オプション	説明
--ffmpeg <パス>	ffmpegのbinフォルダがあるパスを指定できます。 例: --ffmpeg C:\\tools\\ffmpeg\\bin
-o <フォルダ>	出力先フォルダを指定できます。 例: -o C:\\Videos
-f <ファイル名>	出力ファイル名を指定できます。 例: -f myvideo.mp4

### 例
デフォルト設定でダウンロード

python yt2mp4_ytdlp.py "[https://www.youtube.com/watch?v=xxxx](https://www.youtube.com/watch?v=xxxx)"
スクリプトの downloads フォルダに保存されます。

出力先フォルダを指定

python yt2mp4_ytdlp.py "[https://www.youtube.com/watch?v=xxxx](https://www.youtube.com/watch?v=xxxx)" -o "C:\\Videos"
出力ファイル名を指定

python yt2mp4_ytdlp.py "[https://www.youtube.com/watch?v=xxxx](https://www.youtube.com/watch?v=xxxx)" -f "myvideo.mp4"
別の場所にある ffmpeg を使用

python yt2mp4_ytdlp.py "[https://www.youtube.com/watch?v=xxxx](https://www.youtube.com/watch?v=xxxx)" --ffmpeg "D:\\tools\\ffmpeg\\bin"
## ⚠️ 注意事項
著作権に注意し、権利のある動画のみダウンロードしてください。

ffmpeg のパスを間違えると動画の変換に失敗します。

古いWindows Media Playerなどでは再生できないコーデックの動画がダウンロードされる場合があります。

## 📝 ライセンス
このスクリプトは個人利用向けです。商用利用や配布には注意してください。