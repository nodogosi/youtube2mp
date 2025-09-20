#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Windows環境用:
yt-dlpを使ってYouTube動画の音声をMP3に変換して保存するサンプル。
相対パスffmpeg対応。
※著作権に注意し、権利のある動画のみ使用してください。
"""

import os
import sys
import argparse
import yt_dlp

def main():
    # スクリプト自身のあるディレクトリ
    script_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(
        description="Windows用：yt-dlp+ffmpegでYouTube音声をMP3化"
    )
    parser.add_argument("url", help="YouTube動画のURL")
    parser.add_argument(
        "-o", "--outdir", default=".",
        help="出力フォルダ（デフォルト: カレントディレクトリ）"
    )
    parser.add_argument(
        "-f", "--filename", default=None,
        help="出力ファイル名（例: song.mp3）。未指定なら動画タイトルから自動生成"
    )
    parser.add_argument(
        "-b", "--bitrate", default="192",
        help="出力MP3のビットレート（例: 128, 192, 320）"
    )
    parser.add_argument(
        "--ffmpeg",
        default=os.path.join(script_dir, "ffmpeg", "bin"),
        help="ffmpegのbinフォルダ（相対パス可・デフォルト: スクリプトの場所\\ffmpeg\\bin）"
    )

    args = parser.parse_args()

    # ffmpeg相対パス→絶対パスに変換
    ffmpeg_bin_abs = os.path.abspath(args.ffmpeg)
    if not os.path.exists(ffmpeg_bin_abs):
        print(f"ffmpegのフォルダが見つかりません: {ffmpeg_bin_abs}")
        sys.exit(1)

    # ffmpeg.exeとffprobe.exeのパス
    ffmpeg_exe = os.path.join(ffmpeg_bin_abs, "ffmpeg.exe")
    ffprobe_exe = os.path.join(ffmpeg_bin_abs, "ffprobe.exe")
    if not os.path.exists(ffmpeg_exe):
        print(f"ffmpeg.exeが見つかりません: {ffmpeg_exe}")
        sys.exit(1)
    if not os.path.exists(ffprobe_exe):
        print(f"ffprobe.exeが見つかりません: {ffprobe_exe}")
        sys.exit(1)

    print("ffmpeg 設定済み:", ffmpeg_exe)
    print("ffprobe 設定済み:", ffprobe_exe)

    # 出力先フォルダ
    out_dir_abs = os.path.abspath(args.outdir)
    os.makedirs(out_dir_abs, exist_ok=True)

    # 出力テンプレート（ファイル名指定あり／なし）
    if args.filename:
        # 拡張子はyt-dlp側でmp3になる
        outtmpl = os.path.join(out_dir_abs, args.filename)
    else:
        # %(title)s.mp3 形式
        outtmpl = os.path.join(out_dir_abs, "%(title)s.%(ext)s")

    # yt-dlpオプション設定
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': args.bitrate,
        }],
        # ffmpegの場所指定（相対パス対応済み）
        'ffmpeg_location': ffmpeg_bin_abs,
        # 進行状況を表示
        'progress_hooks': [lambda d: print(d['status'], d.get('filename', '')) if d['status'] in ('downloading','finished') else None],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([args.url])
        print("完了しました。出力先フォルダ:", out_dir_abs)
    except Exception as e:
        print("エラー:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
