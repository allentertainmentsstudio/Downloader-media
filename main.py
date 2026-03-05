import os
import threading
import asyncio
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from config import API_ID, API_HASH, BOT_TOKEN
from downloader import download_video
from buttons import quality_buttons
from force_join import check_join

# ---------------- FLASK SERVER ----------------

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---------------- PYROGRAM BOT ----------------

bot = Client(
    "ultimate_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_TEXT = """👋 Hello
📥 Send any video link

Supported:
YouTube
Instagram
TikTok
Facebook
Pinterest
TeraBox
"""

@bot.on_message(filters.command("start"))
async def start(client, message):
    if not await check_join(client, message):
        return
    await message.reply_text(START_TEXT)

@bot.on_message(filters.text & ~filters.command)
async def link_handler(client, message):
    if not await check_join(client, message):
        return
    url = message.text
    await message.reply_text(
        "🎬 Select Quality",
        reply_markup=quality_buttons(url)
    )

@bot.on_callback_query()
async def callback(client, query: CallbackQuery):
    quality, url = query.data.split("|")
    await query.message.edit("⏳ Downloading...")
    try:
        file = download_video(url, quality)
        await query.message.reply_video(file)
        os.remove(file)
        await query.message.delete()
    except Exception as e:
        await query.message.edit("❌ Download failed")

# ---------------- RUN BOT ----------------

def run_bot():
    # Use asyncio.run() to create event loop safely in any thread
    asyncio.run(bot.start())

# ---------------- START BOTH ----------------

if __name__ == "__main__":
    # Telegram bot runs in separate thread
    threading.Thread(target=run_bot).start()
    # Flask runs in main thread
    run_flask()
