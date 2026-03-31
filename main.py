import yt_dlp
import subprocess
import sys


def check_user_command(user_input):
    USER_COMMANDS = ["q", "b"]
    if user_input.lower() in USER_COMMANDS:
        return True

    return False


def user_input_manager(user_input):
    USER_COMMANDS = {"q": sys.exit, "b": search_video}
    if user_input.lower() in USER_COMMANDS:
        USER_COMMANDS[user_input]()


def choice_video_option(url_videos):
    while True:
        user_choice = input("Choice one of the options above(Ex: 1): ")
        if check_user_command(user_choice):
            user_input_manager(user_choice)
        if user_choice in url_videos:
            execute_video(user_choice, url_videos)
            break
        else:
            print("Invalid Command")


def execute_video(user_choice, url_videos):
    command = ["mpv", url_videos[user_choice]]
    subprocess.Popen(command, stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


def search_video():
    VIDEOS_FOUNDED_QUANTITY = 5
    ydl_opts = {
        "quiet": True,
        "format": "bestvideo+bestaudio/best",
        "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        user_input = input("Search: ")
        if check_user_command(user_input):
            user_input_manager(user_input)
        info_data = ydl.extract_info(f"ytsearch{VIDEOS_FOUNDED_QUANTITY}:{user_input}", download=False)

        results = info_data["entries"]
        url_videos = {}

        for index, result in enumerate(results):
            print(f"Index: {index} - Title: {result['title']}")
            url_videos[str(index)] = result['webpage_url']

    return url_videos


while True:
    url_videos = search_video()
    choice_video_option(url_videos)
