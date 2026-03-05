import yt_dlp
import os
from config import DOWNLOAD_DIR

def download_video(url, quality):

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    ydl_opts = {
        "format": f"bestvideo[height<={quality}]+bestaudio/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info)

    return file
