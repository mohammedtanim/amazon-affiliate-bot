import time
import requests
import pandas as pd
from telegram import Bot
from io import StringIO

# Bot Config
BOT_TOKEN = "7691677105:AAFi6VKImrf-tGmMV2J8I1WZS2LOMgaE7PE"
CHANNEL_USERNAME = "@weselltrend24"
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRgAgZKeyNbpRsQevl0eGBZw2X8W0pMXODgyE0029-ueU0QB9pNYF-nO4_adr04dH78qzXDC6_0oVqz/pub?output=csv"
POST_INTERVAL = 1800  # 30 minutes

# Initialize bot
bot = Bot(token=BOT_TOKEN)

def fetch_products():
    response = requests.get(CSV_URL)
    df = pd.read_csv(StringIO(response.text))
    return df

def post_product(product):
    title = product["Product Name"]
    desc = product["Description"]
    image_url = product["Image URL"]
    product_url = product["Product URL"]
    price = product["Price"]
    
    caption = f"🛒 <b>{title}</b>

{desc}

💸 Price: AED{price}
🔗 <a href='{product_url}'>Buy Now</a>

#Amazon #Deals #weselltrend24"
    
    bot.send_photo(
        chat_id=CHANNEL_USERNAME,
        photo=image_url,
        caption=caption,
        parse_mode="HTML"
    )

def main():
    posted = set()
    while True:
        try:
            products = fetch_products()
            for _, product in products.iterrows():
                key = product["Product URL"]
                if key not in posted:
                    post_product(product)
                    posted.add(key)
                    time.sleep(POST_INTERVAL)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
