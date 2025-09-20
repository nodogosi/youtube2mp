#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows環境用：
yt-dlp + ffmpeg を使って YouTube動画を H.264 + AAC のMP4として保存するスクリプト。

※ ffmpeg が ./ffmpeg/bin/ffmpeg.exe にあることを前提としています。
※ 必要に応じてパスを修正してください。
"""

import os
import argparse
import yt_dlp

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description="YouTube動画をH.264 + AACのMP4で保存")
    parser.add_argument("url", help="YouTube動画のURL")
    parser.add_argument(
        "-o", "--out",
        default=os.path.join(script_dir, "downloads"),
        help="出力フォルダ（デフォルト: ./downloads）"
    )
    parser.add_argument(
        "-f", "--filename",
        default="%(title)s.%(ext)s",
        help="出力ファイル名テンプレート（例: %(title)s.%(ext)s）"
    )
    parser.add_argument(
        "--ffmpeg",
        default=os.path.join(script_dir, "ffmpeg", "bin"),
        help="ffmpegのbinフォルダのパス（相対パス可・デフォルト: ./ffmpeg/bin）"
    )
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    ffmpeg_bin = os.path.abspath(args.ffmpeg)
    os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]

    ydl_opts = {
        # H.264 + AAC 優先フォーマット指定
        'format': 'bv*[vcodec^=avc1]+ba[acodec^=mp4a]/b[ext=mp4]',
        # 出力テンプレート
        'outtmpl': os.path.join(args.out, args.filename),
        # ffmpegの場所を指定
        'ffmpeg_location': ffmpeg_bin,
        # 可能ならmp4に変換
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # 最終出力形式
        }],
        # 進捗を表示
        'progress_hooks': [progress_hook],
        'noprogress': False
    }

    print("=== ダウンロード開始 ===")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])
    print("=== 完了 ===")

def progress_hook(d):
    """
    ダウンロード進捗表示用フック
    """
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        print(f"ダウンロード中: {percent} 速度: {speed} ETA: {eta}", end='\r')
    elif d['status'] == 'finished':
        print("\n変換処理を実行中...")

if __name__ == "__main__":
    main()
