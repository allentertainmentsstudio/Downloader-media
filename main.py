import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from config import API_ID, API_HASH, BOT_TOKEN
from downloader import download_video
from buttons import quality_buttons
from force_join import check_join

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


app.run()
