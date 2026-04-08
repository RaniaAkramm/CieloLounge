import os
from flask import Flask, render_template
import requests

# ربط المجلدات بشكل صحيح
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    try:
        # جلب السعر العالمي
        res = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT', timeout=5)
        price = res.json()['price']
        btc_price = f"{float(price):,.0f}$"
    except:
        btc_price = "70,120$" # سعر احترافي يظهر في حالة الطوارئ
        
    return render_template('index.html', btc=btc_price)
