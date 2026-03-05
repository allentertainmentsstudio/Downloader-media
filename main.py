import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from config import API_ID, API_HASH, BOT_TOKEN
from downloader import download_video
from buttons import quality_buttons
from force_join import check_join

# ---------------- PYROGRAM BOT ---------------- #

app = Client(
    "ultimate_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_TEXT = """
👋 Hello

📥 Send any video link

Supported:
YouTube
Instagram
TikTok
Facebook
Pinterest
TeraBox
"""

@app.on_message(filters.command("start"))
async def start(client, message):

    if not await check_join(client, message):
        return

    await message.reply_text(START_TEXT)


@app.on_message(filters.text & ~filters.command)
async def link_handler(client, message):

    if not await check_join(client, message):
        return

    url = message.text

    await message.reply_text(
        "🎬 Select Quality",
        reply_markup=quality_buttons(url)
    )


@app.on_callback_query()
async def callback(client, query: CallbackQuery):

    quality, url = query.data.split("|")

    await query.message.edit("⏳ Downloading...")

    try:
        file = download_video(url, quality)

        await query.message.reply_video(file)

        os.remove(file)

        await query.message.delete()

    except:
        await query.message.edit("❌ Download failed")


# ---------------- FLASK SERVER ---------------- #

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!"


def run_bot():
    app.run()


if __name__ == "__main__":

    # Run Telegram bot in background
    threading.Thread(target=run_bot).start()

    # Run Flask server for Render
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
