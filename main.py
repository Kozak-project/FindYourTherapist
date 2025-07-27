from fastapi import FastAPI
from app.config import TOKEN
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app = FastAPI()

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, how can I help you? (feel free to use any language you want)')


# Response

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'i need help' in processed:
        return 'Ok let\'s begin'

    return 'I don\'t understand what you wrote'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type != 'private':
        return

    print(f'User: {update.message.chat.id} in {message_type}: "{text}"')

    response: str = handle_response(text)

    print(f'Bot: {response}')
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update}, caused error: {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
