import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😂 هلا بيك!\n\n"
        "هذا بوت المقالب الخاص بـ Opito 😎\n"
        "اكتب /prank باش تشوف المقلب."
    )

async def prank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤣🤣 انمسكت!\n\n"
        "كنت متوقع تشوف فيديو، صح؟ 😂"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prank", prank))

    app.run_polling()

if __name__ == "__main__":
    main()
