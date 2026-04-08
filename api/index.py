import os
from flask import Flask, render_template, jsonify
import requests

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

# دالة جلب السعر
def get_btc_price():
    try:
        res = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT', timeout=5)
        price = float(res.json()['price'])
        return f"{price:,.0f}$"
    except:
        return "70,150$"

@app.route('/')
def home():
    return render_template('index.html', btc=get_btc_price())

# هذا هو الرابط الجديد الذي سيستخدمه "زر التحديث"
@app.route('/get_price')
def update_price():
    return jsonify(price=get_btc_price())
