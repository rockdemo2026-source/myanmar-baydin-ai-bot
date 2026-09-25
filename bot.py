import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not configured.")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🔮 မင်္ဂလာပါ!\n\n"
        "မြန်မာ့ဗေဒင် AI Bot မှ ကြိုဆိုပါတယ်။\n\n"
        "မကြာခင်မှာ သင့်ရဲ့ မွေးသက္ကရာဇ်၊ မွေးချိန်၊ "
        "မွေးရပ်အပေါ်မူတည်ပြီး ဗေဒင်ဟောစာများကို "
        "AI ဖြင့် ပြန်လည်ပေးပို့ပေးပါမယ်။"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
