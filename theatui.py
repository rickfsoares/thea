from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input, Button, Label
from textual import work
from textual.containers import HorizontalGroup, VerticalScroll
from logic import fetch_videos, play_video


class Video(HorizontalGroup):

    def __init__(self, url: str, title: str):
        super().__init__()
        self.url = url
        self.title = title

    def play(self):
        play_video(self.url)

    @work(exclusive=True, thread=True)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.play()

    def compose(self) -> ComposeResult:
        yield Label(self.title)
        yield Button("Play", variant="error")


class TheaApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    CSS_PATH = "theatui.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Search for a video", id="video-search")
        yield VerticalScroll(id="videos")

    @work(exclusive=True, thread=True)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.notify(f"Looking for {event.value}")
        urls = fetch_videos(event.value)
        self.call_from_thread(self.query_one('#videos').query(Video).remove)

        for k, v in urls.items():
            video_container = Video(
                url=v["url"], title=v["title"])
            self.call_from_thread(self.query_one(
                "#videos").mount, video_container)
            self.call_from_thread(video_container.scroll_visible)

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = TheaApp()
    app.run()
