import os
from flask import Flask, render_template
import requests

# ربط ملفات التصميم
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    try:
        # جلب السعر مع مهلة انتظار 5 ثواني
        res = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT', timeout=5)
        price = res.json()['price']
        btc_price = f"{float(price):,.0f}$"
    except:
        # سعر افتراضي يظهر في حال انقطاع الإنترنت اللحظي
        btc_price = "70,120$" 
        
    return render_template('index.html', btc=btc_price)
