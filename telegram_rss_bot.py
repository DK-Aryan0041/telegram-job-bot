
import feedparser
import requests
import time

# CONFIG
RSS_FEED_URL = "https://fast2update.in/feed/"
BOT_TOKEN = "8147452008:AAHcmcoX10NfLFXSmFbfFlg7pr5MjHO1CzE"
CHANNEL_ID = "-1001754040945"

last_link = ""

print("Bot started...")

while True:
    try:
        feed = feedparser.parse(RSS_FEED_URL)
        if feed.entries:
            latest = feed.entries[0]
            if latest.link != last_link:
                message = f"🆕 {latest.title}\n{latest.link}"
                response = requests.get(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    params={"chat_id": CHANNEL_ID, "text": message}
                )
                if response.status_code == 200:
                    print("✅ Message sent:", latest.title)
                    last_link = latest.link
                else:
                    print("❌ Failed to send message:", response.text)
        time.sleep(300)  # Check every 5 minutes
    except Exception as e:
        print("⚠️ Error occurred:", e)
        time.sleep(300)
