from pyrogram import __version__
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from bot import Bot
from config import OWNER

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>About this bot: @{client.username}\n○ Creator: @{OWNER}</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Repo by: ©Codexbotz & @mrismanaziz\n\n🧢 Developed by @KayRzky</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• 🔒 Close •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
