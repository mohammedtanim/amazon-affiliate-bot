
import requests, time, csv
from telegram import Bot

BOT_TOKEN = '7691677105:AAFi6VKImrf-tGmMV2J8I1WZS2LOMgaE7PE'
CHANNEL_ID = '@weselltrend24'
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRgAgZKeyNbpRsQevl0eGBZw2X8W0pMXODgyE0029-ueU0QB9pNYF-nO4_adr04dH78qzXDC6_0oVqz/pub?output=csv'

bot = Bot(token=BOT_TOKEN)

def fetch_data():
    response = requests.get(CSV_URL)
    lines = response.text.splitlines()
    reader = csv.DictReader(lines)
    return list(reader)

def post_product(product):
    name = product['Product Name']
    desc = product['Description']
    img = product['Image URL']
    url = product['Product URL']
    price = product['Price']
    caption = f"🛍️ <b>{name}</b>\n\n{desc}\n\n💰 Price: AED {price}\n🔗 <a href='{url}'>Buy Now</a>"
    bot.send_photo(chat_id=CHANNEL_ID, photo=img, caption=caption, parse_mode='HTML')

while True:
    print("Bot is running... Fetching and posting next product.")
    post_product()
    print("Posted. Waiting for 30 minutes...")
    time.sleep(1800)
