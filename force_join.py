from pyrogram.errors import UserNotParticipant
from config import FORCE_CHANNEL

async def check_join(client, message):

    try:
        await client.get_chat_member(FORCE_CHANNEL, message.from_user.id)
        return True

    except UserNotParticipant:
        await message.reply_text(
            f"⚠️ Join our channel first\nhttps://t.me/{FORCE_CHANNEL}"
        )
        return False
