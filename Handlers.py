import os
from pyrogram import Client, filters
from pyrogram.types import Message
from downloader import download_video
from force_join import check_force_join

DOWNLOAD_DIR = "downloads"


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):

    join = await check_force_join(client, message)
    if join is False:
        return

    text = """
👋 Hello

📥 Send me a video link from:

• YouTube  
• Instagram  
• TikTok  
• Facebook  
• Pinterest  
• Twitter / X  
• TeraBox

I will download it and send it to you.
"""
    await message.reply_text(text)


@Client.on_message(filters.text & ~filters.command(["start"]))
async def download_handler(client: Client, message: Message):

    join = await check_force_join(client, message)
    if join is False:
        return

    url = message.text.strip()

    msg = await message.reply_text("⏳ Downloading...")

    try:
        file_path = await download_video(url)

        await message.reply_video(
            video=file_path,
            caption="✅ Download Completed"
        )

        os.remove(file_path)

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")
