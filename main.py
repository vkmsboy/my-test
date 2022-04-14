from pyrogram import Client, filters
from pyrogram.types import Message

Bot=Client(
  "pyrogram bot",
  bot_token="2111463729:AAFYsibwDapnq2gUplJQLeNKHNQvwUGwGoI",
  api_id=17114587,
  api_hash="b1c07d33747425d84050b68bae6be91f"
  )

@Bot.on_message(filters.command("start"))
async def start_message(bot, message):
  await message.reply("Hello 🤗")
  
  
Bot.run()
