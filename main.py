import yt_dlp
import subprocess

ydl_opts = {
    "quiet": True,
    "format": 'bestvideo+bestaudio/best'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    user_input = input("Search: ")
    info_data = ydl.extract_info(f"ytsearch5:{user_input}", download=False)

    results = info_data["entries"]
    url_videos = {}

    for index, result in enumerate(results):
        print(f"Index: {index} - Title: {result['title']}")
        url_videos[str(index)] = result['webpage_url']

    user_choice = input("Choice one of the options above(Ex: 1): ")
    command = ["mpv", url_videos[user_choice]]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

