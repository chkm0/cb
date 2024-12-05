from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Dein Bot-API-Token
BOT_TOKEN = "7549617436:AAG-w1axzryEWuKovNdOMD9mU6JO6hHYtkw"

# Start-Befehl
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hallo! Ich bin dein Bot. Schreib mir eine Nachricht oder sende mir Fotos und Videos!")

# Nachrichten verarbeiten
async def handle_message(update: Update, context: CallbackContext):
    # Nachricht an den Benutzer zurückschicken
    await update.message.reply_text("Danke für deine Nachricht! 😊")

# Medien (Fotos/Videos) verarbeiten
async def handle_media(update: Update, context: CallbackContext):
    if update.message.photo:
        # Foto herunterladen
        photo_file = await update.message.photo[-1].get_file()
        await photo_file.download_to_drive(f"{update.message.chat.id}_photo.jpg")
        await update.message.reply_text("Danke für das Foto! 📷")
    elif update.message.video:
        # Video herunterladen
        video_file = await update.message.video.get_file()
        await video_file.download_to_drive(f"{update.message.chat.id}_video.mp4")
        await update.message.reply_text("Danke für das Video! 🎥")

# Hauptfunktion
def main():
    # Anwendung initialisieren
    application = Application.builder().token(BOT_TOKEN).build()

    # Befehle hinzufügen
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, handle_media))

    # Bot starten
    application.run_polling()

if __name__ == '__main__':
    main()