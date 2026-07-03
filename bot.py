import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")
DESTINATION = "@freebetting_com"

SOURCES = [
    "@Exactscoreking",
    "@bisrat_sport_433et",
    "@sportnewsdailyinfo",
    "@monteirochristian8",
]

logging.basicConfig(level=logging.INFO)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post or update.edited_channel_post
    if not message:
        return
    try:
        await message.forward(chat_id=DESTINATION)
        logging.info(f"✅ Forwarded from {message.chat.username or message.chat.id}")
    except Exception as e:
        logging.error(f"❌ Error: {e}")

def main():
    if not TOKEN:
        logging.error("TOKEN environment variable not set!")
        return
        
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Chat(SOURCES) & ~filters.COMMAND, forward_message))
    
    print("🚀 Bot is running on Render...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()