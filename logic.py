import yt_dlp
import subprocess


def fetch_videos(user_input: str) -> dict:
    VIDEOS_FOUNDED_QUANTITY = 3
    ydl_opts = {
        "quiet": True,
        "format": "bestvideo+bestaudio/best",
        "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_data = ydl.extract_info(f"ytsearch{VIDEOS_FOUNDED_QUANTITY}:{
                                     user_input}", download=False)

        results = info_data["entries"]
        url_videos = {}

        for index, result in enumerate(results):
            # print(f"Index: {index} - Title: {result['title']}")
            url_videos[str(index)] = {
                "url": result['webpage_url'],
                "title": result['title'],
                "thumbnail": result['thumbnail'], }

    return url_videos


def play_video(url: str):
    command = ["mpv", url]
    subprocess.Popen(command, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
