# import os
# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler

# # Load environment variables from .env
# from dotenv import load_dotenv
# load_dotenv()

# # Get your bot token, group ID, and channel ID from the environment
# BOT_TOKEN = os.getenv('BOT_TOKEN')
# GROUP_ID = os.getenv('GROUP_ID')  # The group to listen to
# CHANNEL_ID = os.getenv('CHANNEL_ID')  # The private channel to forward the message

# # Define the function that will handle incoming messages
# async def filter_and_forward(update: Update, context):
#     # Check if the message is from the specified group
#     if update.effective_chat.id == int(GROUP_ID):
#         # Check if the message contains the specific text we're looking for
#         if "5 smart money is buying it!" in update.message.text:
#             # Forward the message to the private channel
#             await context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# async def start(update: Update, context):
#     await update.message.reply_text("Bot is running and listening!")

# if __name__ == '__main__':
#     # Create the application object with your bot's token
#     app = ApplicationBuilder().token(BOT_TOKEN).build()

#     # Add a command handler to check if the bot is working
#     app.add_handler(CommandHandler("start", start))

#     # Add the message handler to filter and forward messages from the group
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_and_forward))

#     # Start polling for new updates (messages)
#     app.run_polling()

import logging
from telethon import TelegramClient, events
from telegram import Bot

# TELEGRAM BOT (polling-based bot)
BOT_TOKEN = "7993754244:AAEANOMBoMdylYnoBFdpS_CcgB_aiIjJAdo"
PRIVATE_CHANNEL_ID = '-1002405855575'  # Replace with the actual channel ID (use negative integer for private channels)

# USERBOT (Telethon-based userbot)
api_id = '21587926'
api_hash = '8e1c7a2b167dbc5ffcc8f56b78c38855'
phone_number = '+2348078470355'
channel_id = '-1002192658770'  # The channel where we listen for messages

# Initialize the Telegram bot object
bot = Bot(token=BOT_TOKEN)

# Initialize the userbot client
userbot_client = TelegramClient('userbot_session', api_id, api_hash)

# Enable logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Define a function to forward a message from userbot to the private channel
async def forward_to_bot(message_text):
    try:
        # Forward the message to the private channel using the bot
        await bot.send_message(chat_id=PRIVATE_CHANNEL_ID, text=message_text)
        logger.info(f"Message forwarded: {message_text}")
    except Exception as e:
        logger.error(f"Error forwarding message: {e}")

# Event handler for new messages in the userbot
@userbot_client.on(events.NewMessage(chats=channel_id))
async def handler(event):
    message_text = event.message.message
    
    # Log the message received from the channel
    logger.info(f"Message received from channel: {message_text}")
    
    # Check if the message contains the required text
    if "5 smart money is buying it!" in message_text:  # Make sure this matches your filter
        logger.info("Trigger text found! Forwarding message...")
        # Forward the filtered message to the bot's private channel
        await forward_to_bot(message_text)
    else:
        logger.info("Message does not contain the trigger text.")

async def main_userbot():
    await userbot_client.start(phone=phone_number)
    logger.info("Userbot is listening to channel messages...")

if __name__ == '__main__':
    # Start the userbot to listen for messages
    with userbot_client:
        userbot_client.loop.run_until_complete(main_userbot())
