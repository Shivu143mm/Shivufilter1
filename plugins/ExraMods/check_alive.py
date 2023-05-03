import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("👊𝐈 𝐀𝐌 𝐏𝐎𝐖𝐄𝐑𝐅𝐔𝐋𝐋 𝐁𝐎𝐓👊
🎥𝐒𝐀𝐑𝐂𝐇 𝐀𝐋𝐋 𝐌𝐎𝐕𝐈𝐄 🎥
🙂𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @SHIVU_143M 🙂
🙂𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 @UPDATE_ALL_MOVIE 🙂")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
