from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7324799687:AAEw5jlN8mzaxI27lNBlSRgabfeszs4Xs8o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Crypto Trends", web_app=WebAppInfo(url="https://zingy-mousse-3a9d9e.netlify.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click below to view live crypto trends:", reply_markup=reply_markup)

app = ApplicationBuilder().token(7324799687:AAEw5jlN8mzaxI27lNBlSRgabfeszs4Xs8o).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
