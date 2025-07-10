
import requests
import time

TOKEN = "7241176410:AAFryZLzGJJfc44GS01djQq4qdy5MbIxTGg"
CHAT_ID = "242888465"
TRADINGVIEW_SYMBOL = "OANDA:XAUUSD"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def get_mock_tradingview_data():
    # Simulasi data (seharusnya scrape atau ambil via API pihak ketiga)
    return {
        "price": 3310.5,
        "stoch_h1": 18.2
    }

def main():
    while True:
        data = get_mock_tradingview_data()
        price = data["price"]
        stoch = data["stoch_h1"]

        if price <= 3312 and stoch < 20:
            message = f"📉 *XAUUSD Buy Limit Alert*\nHarga: {price}\nStochastic H1: {stoch}\n💡 Rekomendasi: Pasang Buy Limit!"
            send_telegram_message(message)
        time.sleep(300)  # cek tiap 5 menit

if __name__ == "__main__":
    main()
