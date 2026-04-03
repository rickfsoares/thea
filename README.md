# 🎥 Thea - Minimalist YouTube TUI

A fast, distraction-free YouTube search and playback interface built for the terminal.

## 📖 About the Project

Thea is a Terminal User Interface (TUI) designed for users who prefer the efficiency of the command line over heavy web browsers.
By leveraging the power of Python, Textual, and MPV, Thea provides a streamlined workflow to find and watch content with minimal resource overhead.

### ✨ Key Features

- 🔍 Focused Search: Instant results directly in your terminal buffer.

- 🚀 Resource Efficient: Uses significantly less RAM and CPU than a standard web browser.

- 🛡️ Privacy-First: Minimal data tracking by bypassing complex web player scripts.

- 🌓 Adaptive UI: Full support for Dark and Light modes.

- 🧵 Responsive Design: Built with an asynchronous architecture to ensure the UI never freezes during data fetching.

## 🛠 Prerequisites
To ensure Thea runs smoothly, you must have the following system-level tools installed:

    1. Python 3.8+

    2. yt-dlp: The engine for metadata extraction.

    3. mpv: The core media player for high-quality streaming.

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/rickfsoares/thea.git
cd thea

# 2. Set up a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt
```

## 🎮 Usage

Launch the application with:

```bash
python app.py
```

## 📂 Project Structure

- app.py: The Textual-based UI and event handling.

- logic.py: The core engine interfacing with yt-dlp and mpv.

- theatui.tcss: Modern CSS-like styling for the terminal interface.

- requirements.txt: Necessary Python packages (Textual, etc.).

## ⚖️ Disclaimer

This project is intended for educational purposes and personal use only. Thea is a third-party interface and is not affiliated with, authorized, maintained, sponsored, or endorsed by YouTube or any of its affiliates. Users are responsible for complying with the YouTube Terms of Service and respecting content creators rights.

## 📝 License
Distributed under the MIT License. See License for more details.
