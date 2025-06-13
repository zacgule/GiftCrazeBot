import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your BotFather token
TOKEN = ""

# Configuration - replace with your actual links
REDIRECT_LINKS = {
    "apk": "https://t.me/MODAPPSKING",
    "database": "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/d/leaks", 
    "hacking": "https://t.me/CyberNirvana/1",
    "forum": "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/post/71514fc4e91f97631a8b",
    "channel": "https://t.me/hackertale",  # Support my channel because we adhere to ethical hacking practices
    "group": "https://t.me/kazelsecretsociety" # Support my group because that is how I can continue to educate dangerrs about telegram bots 
}

# Ethical warning message (appears in all responses)
ETHICAL_WARNING = (
    "⚠️ 預先警告！ETHICAL USE ONLY: This bot demonstrates how easily malicious actors "
    "can distribute dangerous content. Never use these techniques illegally!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message with interactive keyboard"""
    user = update.effective_user
    welcome_msg = (
        f"👋 Greetings {user.first_name}! I'm a digital treasure chest...\n\n"
        "💎 But beware - look out  what you are asking for!\n\n"
        f"{ETHICAL_WARNING}\n\n"
        "🌐 Support ethical hacking and join our community!\n"
        f"- Telegram Channel: {REDIRECT_LINKS['channel']}\n"
        f"- Group Chat: {REDIRECT_LINKS['group']}\n"
    )
    keyboard = [
        [InlineKeyboardButton("Give me free modified apk", callback_data='apk')],
        [InlineKeyboardButton("Give me leaked database", callback_data='database')],
        [InlineKeyboardButton("Give me dangerous hacking treats", callback_data='hacking')],
        [InlineKeyboardButton("🎁 Hacker Forums Gift", callback_data='forum')],
        [InlineKeyboardButton("📢 Join Channel", url=REDIRECT_LINKS['channel'])],
        [InlineKeyboardButton("💬 Join Group", url=REDIRECT_LINKS['group'])],
        [InlineKeyboardButton("🚪 Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Always use reply_text for /start, edit_message_text for return
    if update.message:
        await update.message.reply_text(welcome_msg, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(welcome_msg, reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process button presses"""
    query = update.callback_query
    await query.answer()  # Api works here to fetch the query data    
    choice = query.data
    
    # Handle exit option
    if choice == 'exit':
        await query.edit_message_text(
            text="💨 Thank you for trying the bot! Stay safe and remember: Real treasures are earned, not stolen! 🏴‍☠️"
        )
        return
    
    # Define responses for each risky option , so you guys don't click on sus links to get into trouble
    responses = {
        'apk': (
            "🛡️ Security Alert:\n"
            "Modified APKs often contain malware that can:\n"
            "- Steal your credentials\n"
            "- Encrypt your data for ransom\n"
            "- Turn your device into a botnet zombie\n\n"
            f"🔗 Proceed at your own risk: {REDIRECT_LINKS['apk']}"
        ),
        'database': (
            "🔥 High Risk Warning:\n"
            "Leaked databases are:\n"
            "- Often illegal to possess\n"
            "- Used for identity theft\n"
            "- Frequently booby-trapped by law enforcement\n\n"
            f"🔗 Dangerous path: {REDIRECT_LINKS['database']}"
        ),
        'hacking': (
            "☢️ EXTREME DANGER:\n"
            "Unmonitored Hacking tools can:\n"
            "- Get you arrested if it is not adhering to legal and ethical uses\n"
            "- Destroy your system\n"
            "- Expose you to criminal prosecution\n\n"
            f"🔗 Enter the dragon's den: {REDIRECT_LINKS['hacking']}"
        ),
        'forum': (
            "🎁 Hacker Forums Gift:\n"
            "Access some of the most popular hacker forums (for educational purposes only):\n"
            f"🔗 {REDIRECT_LINKS['forum']}\n\n"
            "Use responsibly and ethically!\n\n"
        )
    }
    
    # Send response with ethical warning
    if choice in responses:
        response_text = (
            f"{responses[choice]}\n\n"
            f"{ETHICAL_WARNING}\n\n"
            "💎 Thank you for helping demonstrate why you should NEVER trust random Telegram bots!千萬唔好輕易相信Telegram Bots"
        )
        keyboard = [
            [InlineKeyboardButton("⬅️ Return to Menu", callback_data='return')],
            [InlineKeyboardButton("🚪 Exit", callback_data='exit')]
        ]
        await query.edit_message_text(response_text, reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True)
    elif choice == 'return':
        # On return, always show the main menu as an edit (not reply)
        await start(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_button))
    logger.info("Giftcraze Bot is now running...")
    application.run_polling()

if __name__ == '__main__':
    main()