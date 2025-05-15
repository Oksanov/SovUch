import os
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# === Telegram-бот ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m your bot running on Render with Flask.")

# Создаём Telegram-приложение
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# === Flask-сервер ===
flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "✅ Telegram bot is running on Render."

# === Запуск обоих приложений ===
def run_telegram_bot():
    telegram_app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_telegram_bot).start()
    flask_app.run(host="0.0.0.0", port=10000)