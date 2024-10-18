import logging
from telethon import TelegramClient, events
from telegram import Bot

# TELEGRAM BOT (polling-based bot)
BOT_TOKEN = "7993754244:AAEANOMBoMdylYnoBFdpS_CcgB_aiIjJAdo"  # Replace with your actual bot token
PRIVATE_CHANNEL_ID = '-1002405855575'  # Replace with your private channel's actual ID

# USERBOT (Telethon-based userbot credentials)
api_id = '21587926'  # Your API ID
api_hash = '8e1c7a2b167dbc5ffcc8f56b78c38855'  # Your API hash
phone_number = '+2348078470355'  # Your Telegram phone number (with country code)

# The group/channel where we listen for messages (group you're monitoring)
group_id = 't.me/MEME1000XMFS'  # Channel/group you're monitoring

# Initialize the Telegram bot object
bot = Bot(token=BOT_TOKEN)

# Initialize the userbot client (Telethon)
userbot_client = TelegramClient('userbot_session', api_id, api_hash)

# Enable logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Define a function to forward the message from the userbot to the private channel
async def forward_to_bot(message_text):
    try:
        # Forward the message to the private channel using the bot
        bot.send_message(chat_id=PRIVATE_CHANNEL_ID, text=message_text)
        logger.info(f"Message forwarded to private channel: {message_text}")
    except Exception as e:
        logger.error(f"Error forwarding message: {e}")

# Event handler for new messages in the userbot
@userbot_client.on(events.NewMessage(chats=group_id))
async def handler(event):
    message_text = event.message.message
    
    # Log the message received from the group
    logger.info(f"Message received from group: {message_text}")
    
    # Check if the message contains the required text
    if "5 smart money is buying it!" in message_text:
        logger.info("Trigger text found! Forwarding message...")
        # Forward the filtered message to the bot's private channel
        await forward_to_bot(message_text)
    else:
        logger.info("Message does not contain the trigger text.")

# Function to start the userbot client
async def main_userbot():
    await userbot_client.start(phone=phone_number)
    logger.info("Userbot is listening to group messages...")

if __name__ == '__main__':
    # Start the userbot to listen for messages
    with userbot_client:
        userbot_client.loop.run_until_complete(main_userbot())
