import os
from flask import Flask, render_template, jsonify
import requests

# إعداد المسارات
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

# دالة لجلب السعر المباشر من باينانس
def fetch_binance_price(symbol="BTCUSDT"):
    try:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url, timeout=5)
        data = response.json()
        price = float(data['price'])
        # تنسيق الرقم ليكون بفاصلة آلاف وصفرين بعد الفاصلة
        return f"{price:,.2f}$"
    except:
        return "Market Busy"

@app.route('/')
def home():
    # جلب السعر عند أول تحميل للصفحة
    return render_template('index.html', btc=fetch_binance_price())

@app.route('/get_price')
def update_price():
    # الرابط الذي سيستخدمه الموقع للتحديث التلقائي كل 5 ثوانٍ
    return jsonify(price=fetch_binance_price())
