🚀 Ultimate Telegram Downloader Bot

A powerful Telegram bot built with Python + Pyrogram that can download videos from multiple websites and send them directly to Telegram.

---

📥 Supported Platforms

This bot can download videos from:

- YouTube
- Instagram
- TikTok
- Facebook
- Pinterest
- Twitter / X
- TeraBox (basic support)

Powered by yt-dlp, which supports 1000+ websites.

---

✨ Features

- 🎬 Video Quality Selection (360p / 720p / 1080p)
- 📥 Fast Video Downloader
- 🔐 Force Join Channel System
- 📁 Auto Delete Downloaded Files
- ⚡ Simple and Fast
- 📦 Up to 2GB File Upload Support
- 🧩 Modular Code Structure

---

📂 Project Structure

ultimate-downloader-bot
│
├── main.py
├── config.py
├── downloader.py
├── terabox.py
├── buttons.py
├── force_join.py
├── requirements.txt
└── Dockerfile

---

⚙️ Environment Variables

Set the following environment variables before running the bot.

API_ID=
API_HASH=
BOT_TOKEN=
FORCE_CHANNEL=

Example:

API_ID=12345678
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=1234567890:ABCDefGhIjKlMnOpQrStUvWxYz
FORCE_CHANNEL=MyTelegramChannel

---

🛠 Installation (Local)

1. Clone the repository

git clone https://github.com/allentertainmentsstudio/Downloader-media.git

2. Go to project folder

cd ultimate-downloader-bot

3. Install requirements

pip install -r requirements.txt

4. Run the bot

python main.py

---

🐳 Deploy with Docker

Build image:

docker build -t downloader-bot .

Run container:

docker run downloader-bot

---

☁ Deploy on Render

1. Push this project to GitHub
2. Go to Render
3. Create a new Web Service
4. Connect your GitHub repository
5. Add Environment Variables
6. Deploy 🚀

---

📜 Requirements

pyrogram
tgcrypto
yt-dlp
requests

---

⚠️ Disclaimer

This bot is intended for educational purposes only.
Make sure you follow the terms of service of the platforms you download content from.

---

👨‍💻 Author

Telegram Downloader Bot made using Python & Pyrogram.
