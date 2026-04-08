import os
from flask import Flask, render_template
import requests

# هذا السطر يخبر البرنامج بمكان مجلد templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    try:
        # جلب سعر البيتكوين
        response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        price = response.json()['price']
        btc_price = f"{float(price):,.2f}$"
    except:
        btc_price = "جاري التحديث..."
        
    return render_template('index.html', btc=btc_price)

# سطر مهم لمنصة Vercel
app.debug = True
