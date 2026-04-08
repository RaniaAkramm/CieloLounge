import os
from flask import Flask, render_template

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usd')
def usd_hub():
    # سنضع هنا لاحقاً كود جدول الدولار
    return "USD Market List - Coming Soon"

@app.route('/eur')
def eur_hub():
    return "EUR Market List - Coming Soon"

# يمكنك إضافة بقية المسارات هنا لاحقاً
