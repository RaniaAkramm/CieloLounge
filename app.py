from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # جلب سعر البيتكوين من باينانس مجاناً
        response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        price = response.json()['price']
        btc_price = f"{float(price):,.2f}$"
    except:
        btc_price = "جاري التحديث..."
        
    return render_template('index.html', btc=btc_price)
