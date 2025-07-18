import asyncio
import logging
import random
from aiohttp import ClientSession
from aiogram import Bot, Dispatcher, types

API_TOKEN = "7946365086:AAEQgHfvEhxW9a-IYQI1DjcNcu_TmlOfcSY"
CHANNEL_ID = "@weselltrend24"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Verified working images from Amazon
PRODUCTS = [
    {
        "title": "🔥 Bluetooth Headphones",
        "url": "https://www.amazon.in/dp/B09PZ9GPQM?tag=weselltrend24-21",
        "image": "https://m.media-amazon.com/images/I/71BM3Xdfg1L._AC_SL1500_.jpg",
        "description": "Top-rated sound and comfort for your daily tunes!"
    },
    {
        "title": "✨ Bestseller Smart Watch",
        "url": "https://www.amazon.in/dp/B0B5MLDSHR?tag=weselltrend24-21",
        "image": "https://m.media-amazon.com/images/I/61vXcZUfVwL._AC_SL1500_.jpg",
        "description": "Track steps, heart rate, and more – in style!"
    },
    {
        "title": "💡 LED Touch Lamp",
        "url": "https://www.amazon.in/dp/B084Q4S2MY?tag=weselltrend24-21",
        "image": "https://m.media-amazon.com/images/I/61gxa1LmuZL._AC_SL1500_.jpg",
        "description": "Touch control lamp with USB charging port."
    },
]

async def post_product(bot: Bot, session: ClientSession):
    try:
        product = random.choice(PRODUCTS)
        caption = f"{product['title']}\n\n{product['description']}\n\n🔗 [Buy Now]({product['url']})"

        # 🛡 Try to post image
        async with session.get(product["image"]) as response:
            if response.status == 200:
                await bot.send_photo(
                    chat_id=CHANNEL_ID,
                    photo=product["image"],
                    caption=caption,
                    parse_mode=types.ParseMode.MARKDOWN
                )
            else:
                # 📩 Fallback to text if image fails
                await bot.send_message(
                    chat_id=CHANNEL_ID,
                    text=caption,
                    parse_mode=types.ParseMode.MARKDOWN
                )

        logger.info("✅ Posted successfully!")

    except Exception as e:
        logger.error(f"❌ Error posting: {e}")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    session = ClientSession()

    logger.info("🚀 Bot started. Posting every 60 minutes.")
    try:
        while True:
            await post_product(bot, session)
            logger.info("⏳ Waiting 60 minutes for next round...")
            await asyncio.sleep(60 * 60)
    finally:
        await bot.session.close()
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())
