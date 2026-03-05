🚀 Ultimate Telegram Downloader Bot

"Python" (https://img.shields.io/badge/Python-3.10+-blue.svg)
"Pyrogram" (https://img.shields.io/badge/Library-Pyrogram-green)
"License" (https://img.shields.io/badge/License-MIT-yellow)
"Stars" (https://img.shields.io/github/stars/allentertainmentsstudio/Downloader-media?style=social)

A powerful Telegram Downloader Bot built with Python + Pyrogram that can download videos and media from multiple platforms and send them directly to Telegram.

---

📥 Supported Platforms

This bot can download media from:

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
- ⚡ Fast Download Speed
- 📥 Direct Upload to Telegram
- 🔐 Force Join Channel System
- 📁 Auto Delete Downloaded Files
- 🧩 Modular Code Structure
- 📦 Up to 2GB File Upload Support

---

🤖 Telegram Bot

You can create your bot using @BotFather.

Start your bot like this:

/start

Then send any video link and the bot will download it.

---

📂 Project Structure

Downloader-media
│
├── main.py
├── config.py
├── handlers.py
├── downloader.py
├── terabox.py
├── buttons.py
├── force_join.py
├── requirements.txt
├── Dockerfile
└── README.md

---

⚙️ Environment Variables

Create a ".env" file or add these variables in your hosting platform.

API_ID=
API_HASH=
BOT_TOKEN=
FORCE_CHANNEL=

Example

API_ID=123456
API_HASH=abcd1234abcd1234abcd1234abcd1234
BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
FORCE_CHANNEL=@yourchannel

---

📦 Installation

1️⃣ Clone the repository

git clone https://github.com/allentertainmentsstudio/Downloader-media.git

2️⃣ Go to the project folder

cd Downloader-media

3️⃣ Install requirements

pip install -r requirements.txt

4️⃣ Run the bot

python main.py

---

🐳 Docker Deployment

Build Docker image

docker build -t downloader-bot .

Run container

docker run -d downloader-bot

---

☁️ Deploy on Render

1. Go to https://render.com
2. Click New Web Service
3. Connect your GitHub repository
4. Add Environment Variables
5. Click Deploy

Start Command:

python main.py

---

📜 Requirements

pyrogram
tgcrypto
yt-dlp
requests

---

⚠️ Disclaimer

This bot is for educational purposes only.
Make sure you follow the terms of service of the platforms you download content from.

---

⭐ Support

If you like this project, please give it a star ⭐ on GitHub.

---

👨‍💻 Developer

Maintained by Allen Entertainment Studio

GitHub:
https://github.com/allentertainmentsstudio
