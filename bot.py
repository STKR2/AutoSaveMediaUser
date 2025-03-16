import os
from pyrogram import Client, filters
import asyncio

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

@app.on_message(filters.photo | filters.video & filters.private)
async def handle_media(client, message):
    if message.photo:
        file = await message.download()
        caption = f"- تم حفظ الصـورة بنجاح .\n- من : @{message.from_user.username}" if message.from_user.username else "من: مستخدم مجهول"
        await client.send_photo("me", file, caption=caption)
    elif message.video:
        file = await message.download()
        caption = f"- تم حفظ الفيـديو بنجاح .\n- من : @{message.from_user.username}" if message.from_user.username else "من: مستخدم مجهول"
        await client.send_video("me", file, caption=caption)
    await client.send_message("me", "")

async def main():
    await app.start()
    print("Bot is running...")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
