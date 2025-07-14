from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

coins = {
    "BTC/USDT": "Strong Buy",
    "ETH/USDT": "Buy",
    "DOGE/USDT": "Sell",
    "ADA/USDT": "Strong Sell"
}

@app.route('/')
def home():
    return "<h2>✅ Crypto Trend History API is Live</h2>"

@app.route('/get-history', methods=['GET'])
def get_history():
    coin = request.args.get("coin", "BTC/USDT")
    trend = coins.get(coin, "No Trend")
    history = []
    base_price = random.uniform(100, 3000)
    for i in range(5):
        day = datetime.today() - timedelta(days=i)
        price = base_price + random.uniform(-0.05, 0.05) * base_price
        history.append({
            "date": day.strftime("%Y-%m-%d"),
            "price": round(price, 2)
        })
    return jsonify({
        "coin": coin,
        "trend": trend,
        "history": history[::-1]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
