from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def quality_buttons(url):

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("360p", callback_data=f"360|{url}"),
                InlineKeyboardButton("720p", callback_data=f"720|{url}")
            ],
            [
                InlineKeyboardButton("1080p", callback_data=f"1080|{url}")
            ]
        ]
    )
