import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Данные бота
TELEGRAM_BOT_TOKEN = "8426301021:AAGUUiVphycTOJ8EBesLYdspe_kszY7vBIM"
TELEGRAM_CHAT_ID = "-5417434895"  # ID группы (обычно начинается с -100...)


def send_telegram_message(text):
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
  payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
  return requests.post(url, json=payload)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/api/order", methods=["POST"])
def create_order():
  data = request.json

  # Формируем красивое сообщение для менеджера
  message = (
      "🛍 <b>НОВЫЙ ЗАКАЗ С САЙТА!</b>\n\n"
      f"👤 <b>Клиент:</b> {data.get('name')}\n"
      f"📞 <b>Телефон:</b> {data.get('phone')}\n"
      f"🚚 <b>Доставка:</b> {data.get('delivery_service')} ({data.get('address')})\n\n"
      f"📦 <b>Заказ:</b>\n{data.get('items_text')}\n\n"
      f"💰 <b>Итого к оплате:</b> {data.get('total_price')} грн"
  )

  response = send_telegram_message(message)

  if response.status_code == 200:
    return jsonify({"status": "success", "message": "Заказ принят!"}), 200
  else:
    return jsonify({"status": "error", "message": "Ошибка отправки"}), 500


if __name__ == "__main__":
  app.run(debug=True, port=5000)
