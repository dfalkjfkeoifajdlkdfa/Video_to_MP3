from yt_dlp import YoutubeDL

ydl_opts = {
    "outtmpl": "~/Downloads/%(title)s.%(ext)s",
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "http_headers": {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    },
    "extractor_args": {
        "youtube": {
            "player_client": ["tv_embedded"]
        }
    },
    "ffmpeg_location": "/opt/homebrew/bin"
}

urls = [
    ""

]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

