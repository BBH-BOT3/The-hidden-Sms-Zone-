#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The hidden Sms Zone - Telegram Bot v2
Telegram গ্রুপে কোড পাঠানোর ফিচার সহ
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import json
from datetime import datetime

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ডেটা স্টোর করার জন্য ডিকশনারি
user_data = {}

# ⚠️ গুরুত্বপূর্ণ: আপনার গ্রুপ ID এখানে সেট করুন
# গ্রুপ ID পেতে: @userinfobot এ /start পাঠান, তারপর গ্রুপে ফরওয়ার্ড করুন
ADMIN_GROUP_ID = -5532501478  # আপনার গ্রুপ ID এখানে রাখুন (নেগেটিভ সংখ্যা)

# সমস্ত দেশ এবং তাদের নাম্বার প্রিফিক্স
COUNTRIES = {
    "🇧🇩 Bangladesh": {
        "code": "+880",
        "flag": "🇧🇩",
        "numbers": [
            "+8801700000001", "+8801700000002", "+8801700000003", "+8801700000004",
            "+8801800000001", "+8801800000002", "+8801800000003", "+8801800000004",
            "+8801900000001", "+8801900000002", "+8801900000003", "+8801900000004"
        ]
    },
    "🇮🇳 India": {
        "code": "+91",
        "flag": "🇮🇳",
        "numbers": [
            "+919000000001", "+919000000002", "+919000000003", "+919000000004",
            "+919100000001", "+919100000002", "+919200000001", "+919200000002",
            "+919300000001", "+919300000002", "+919400000001", "+919400000002"
        ]
    },
    "🇵🇰 Pakistan": {
        "code": "+92",
        "flag": "🇵🇰",
        "numbers": [
            "+923000000001", "+923000000002", "+923000000003", "+923000000004",
            "+923100000001", "+923100000002", "+923200000001", "+923200000002",
            "+923300000001", "+923300000002", "+923400000001", "+923400000002"
        ]
    },
    "🇿🇲 Zambia": {
        "code": "+260",
        "flag": "🇿🇲",
        "numbers": [
            "+260755383425", "+260755383426", "+260755383427", "+260755383428",
            "+260765000001", "+260765000002", "+260765000003", "+260765000004",
            "+260770000001", "+260770000002", "+260770000003", "+260770000004"
        ]
    },
    "🇺🇬 Uganda": {
        "code": "+256",
        "flag": "🇺🇬",
        "numbers": [
            "+256700000001", "+256700000002", "+256700000003", "+256700000004",
            "+256750000001", "+256750000002", "+256750000003", "+256750000004",
            "+256760000001", "+256760000002", "+256760000003", "+256760000004"
        ]
    },
    "🇰🇪 Kenya": {
        "code": "+254",
        "flag": "🇰🇪",
        "numbers": [
            "+254700000001", "+254700000002", "+254700000003", "+254700000004",
            "+254710000001", "+254710000002", "+254720000001", "+254720000002",
            "+254730000001", "+254730000002", "+254740000001", "+254740000002"
        ]
    },
    "🇬🇭 Ghana": {
        "code": "+233",
        "flag": "🇬🇭",
        "numbers": [
            "+233500000001", "+233500000002", "+233500000003", "+233500000004",
            "+233510000001", "+233510000002", "+233520000001", "+233520000002",
            "+233530000001", "+233530000002", "+233540000001", "+233540000002"
        ]
    },
    "🇳🇬 Nigeria": {
        "code": "+234",
        "flag": "🇳🇬",
        "numbers": [
            "+234800000001", "+234800000002", "+234800000003", "+234800000004",
            "+234810000001", "+234810000002", "+234820000001", "+234820000002",
            "+234830000001", "+234830000002", "+234840000001", "+234840000002"
        ]
    },
    "🇪🇹 Ethiopia": {
        "code": "+251",
        "flag": "🇪🇹",
        "numbers": [
            "+251900000001", "+251900000002", "+251900000003", "+251900000004",
            "+251910000001", "+251910000002", "+251920000001", "+251920000002",
            "+251930000001", "+251930000002", "+251940000001", "+251940000002"
        ]
    },
    "🇲🇿 Mozambique": {
        "code": "+258",
        "flag": "🇲🇿",
        "numbers": [
            "+258840000001", "+258840000002", "+258840000003", "+258840000004",
            "+258850000001", "+258850000002", "+258860000001", "+258860000002",
            "+258870000001", "+258870000002", "+258880000001", "+258880000002"
        ]
    }
}

# প্ল্যাটফর্ম সমূহ
PLATFORMS = {
    "facebook": {"name": "📘 Facebook", "emoji": "📘"},
    "whatsapp": {"name": "💬 WhatsApp", "emoji": "💬"},
    "instagram": {"name": "📷 Instagram", "emoji": "📷"},
    "tiktok": {"name": "🎵 TikTok", "emoji": "🎵"},
    "telegram": {"name": "✈️ Telegram", "emoji": "✈️"}
}

def generate_otp():
    """র্যান্ডম OTP জেনারেট করা"""
    return str(random.randint(100000, 999999))

async def send_code_to_group(context: ContextTypes.DEFAULT_TYPE, user_id: int, 
                             user_name: str, country: str, platform: str, 
                             number: str, otp: str) -> None:
    """গ্রুপে কোড পাঠানো"""
    try:
        message = f"""
📱 **নতুন নাম্বার অনুরোধ**

👤 **ব্যবহারকারী:** {user_name} (ID: {user_id})
🌍 **দেশ:** {country}
💻 **প্ল্যাটফর্ম:** {platform}
📞 **নাম্বার:** `{number}`
🔐 **OTP/কোড:** `{otp}`
⏰ **সময়:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        await context.bot.send_message(
            chat_id=ADMIN_GROUP_ID,
            text=message,
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"গ্রুপে মেসেজ পাঠাতে ত্রুটি: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """স্টার্ট কমান্ড হ্যান্ডলার"""
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    
    # ইউজার ডেটা ইনিশিয়ালাইজ করা
    if user_id not in user_data:
        user_data[user_id] = {
            "country": None,
            "platform": None,
            "number": None,
            "otp": None,
            "timestamp": datetime.now().isoformat()
        }
    
    welcome_text = f"""
🎯 **স্বাগতম {user_name}! The hidden Sms Zone এ**

আমরা আপনাকে বিভিন্ন দেশের ভার্চুয়াল নাম্বার প্রদান করি যা দিয়ে আপনি:
✅ Facebook অ্যাকাউন্ট খুলতে পারবেন
✅ WhatsApp অ্যাকাউন্ট খুলতে পারবেন
✅ Instagram অ্যাকাউন্ট খুলতে পারবেন
✅ TikTok অ্যাকাউন্ট খুলতে পারবেন
✅ Telegram অ্যাকাউন্ট খুলতে পারবেন

শুরু করতে নিচের বাটন ক্লিক করুন:
"""
    
    keyboard = [
        [InlineKeyboardButton("🌍 দেশ নির্বাচন করুন", callback_data="select_country")],
        [InlineKeyboardButton("📊 সক্রিয় নাম্বার", callback_data="active_numbers")],
        [InlineKeyboardButton("❓ সাহায্য", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

async def select_country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """দেশ নির্বাচন মেনু"""
    query = update.callback_query
    await query.answer()
    
    text = "🌍 **দেশ নির্বাচন করুন:**\n\n"
    
    keyboard = []
    for idx, country in enumerate(COUNTRIES.keys(), 1):
        keyboard.append([InlineKeyboardButton(country, callback_data=f"country_{idx}")])
    
    # ব্যাক বাটন
    keyboard.append([InlineKeyboardButton("⬅️ ফিরে যান", callback_data="back_to_main")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def select_platform(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """প্ল্যাটফর্ম নির্বাচন মেনু"""
    query = update.callback_query
    user_id = query.from_user.id
    
    await query.answer()
    
    text = f"💻 **প্ল্যাটফর্ম নির্বাচন করুন:**\n\n"
    
    keyboard = [
        [InlineKeyboardButton(PLATFORMS["facebook"]["name"], callback_data="platform_facebook")],
        [InlineKeyboardButton(PLATFORMS["whatsapp"]["name"], callback_data="platform_whatsapp")],
        [InlineKeyboardButton(PLATFORMS["instagram"]["name"], callback_data="platform_instagram")],
        [InlineKeyboardButton(PLATFORMS["tiktok"]["name"], callback_data="platform_tiktok")],
        [InlineKeyboardButton(PLATFORMS["telegram"]["name"], callback_data="platform_telegram")],
        [InlineKeyboardButton("⬅️ ফিরে যান", callback_data="select_country")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def show_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """নাম্বার প্রদর্শন এবং গ্রুপে পাঠানো"""
    query = update.callback_query
    user_id = query.from_user.id
    user_name = query.from_user.first_name
    
    await query.answer()
    
    if user_id not in user_data:
        user_data[user_id] = {
            "country": None,
            "platform": None,
            "number": None,
            "otp": None
        }
    
    country_name = user_data[user_id].get("country")
    platform_name = user_data[user_id].get("platform")
    
    if not country_name or not platform_name:
        await query.edit_message_text("❌ দয়া করে প্রথমে দেশ এবং প্ল্যাটফর্ম নির্বাচন করুন।")
        return
    
    # র্যান্ডম নাম্বার নির্বাচন
    country_data = COUNTRIES[country_name]
    selected_number = random.choice(country_data["numbers"])
    
    # OTP জেনারেট করা
    otp = generate_otp()
    
    # ইউজার ডেটা আপডেট করা
    user_data[user_id]["number"] = selected_number
    user_data[user_id]["otp"] = otp
    
    # গ্রুপে কোড পাঠানো
    await send_code_to_group(context, user_id, user_name, country_name, 
                            platform_name, selected_number, otp)
    
    text = f"""
✅ **সক্রিয় নাম্বার**

🌍 **দেশ:** {country_name}
💻 **প্ল্যাটফর্ম:** {platform_name}
📱 **নাম্বার:** `{selected_number}`

⏰ **সময়:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📌 **গুরুত্বপূর্ণ:** আপনার OTP আমাদের প্রাইভেট গ্রুপে পাঠানো হয়েছে। আপনি সেখান থেকে কোড দেখতে পারবেন।
"""
    
    keyboard = [
        [InlineKeyboardButton("🔄 নাম্বার পরিবর্তন করুন", callback_data="change_number")],
        [InlineKeyboardButton("🔀 প্ল্যাটফর্ম পরিবর্তন করুন", callback_data="select_platform")],
        [InlineKeyboardButton("🏠 হোম", callback_data="back_to_main")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def change_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """নাম্বার পরিবর্তন করা"""
    query = update.callback_query
    user_id = query.from_user.id
    user_name = query.from_user.first_name
    
    await query.answer()
    
    if user_id not in user_data:
        await query.edit_message_text("❌ কোন নাম্বার পাওয়া যায়নি।")
        return
    
    country_name = user_data[user_id].get("country")
    platform_name = user_data[user_id].get("platform")
    
    if not country_name or not platform_name:
        await query.edit_message_text("❌ দয়া করে প্রথমে দেশ এবং প্ল্যাটফর্ম নির্বাচন করুন।")
        return
    
    # নতুন নাম্বার নির্বাচন
    country_data = COUNTRIES[country_name]
    new_number = random.choice(country_data["numbers"])
    new_otp = generate_otp()
    
    user_data[user_id]["number"] = new_number
    user_data[user_id]["otp"] = new_otp
    
    # গ্রুপে নতুন কোড পাঠানো
    await send_code_to_group(context, user_id, user_name, country_name, 
                            platform_name, new_number, new_otp)
    
    text = f"""
✅ **নাম্বার পরিবর্তিত হয়েছে**

🌍 **দেশ:** {country_name}
💻 **প্ল্যাটফর্ম:** {platform_name}
📱 **নতুন নাম্বার:** `{new_number}`

⏰ **সময়:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📌 **গুরুত্বপূর্ণ:** আপনার নতুন OTP আমাদের প্রাইভেট গ্রুপে পাঠানো হয়েছে।
"""
    
    keyboard = [
        [InlineKeyboardButton("🔄 আবার পরিবর্তন করুন", callback_data="change_number")],
        [InlineKeyboardButton("🔀 প্ল্যাটফর্ম পরিবর্তন করুন", callback_data="select_platform")],
        [InlineKeyboardButton("🏠 হোম", callback_data="back_to_main")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def active_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """সক্রিয় নাম্বার প্রদর্শন"""
    query = update.callback_query
    
    await query.answer()
    
    text = "📊 **সক্রিয় নাম্বার সমূহ**\n\n"
    text += "আমাদের বর্তমানে নিম্নলিখিত দেশগুলিতে সক্রিয় নাম্বার রয়েছে:\n\n"
    
    for idx, country in enumerate(COUNTRIES.keys(), 1):
        text += f"{idx}. {country}\n"
    
    text += f"\n\n**মোট দেশ:** {len(COUNTRIES)}\n"
    text += "**মোট নাম্বার:** " + str(sum(len(COUNTRIES[c]["numbers"]) for c in COUNTRIES))
    
    keyboard = [
        [InlineKeyboardButton("🌍 দেশ নির্বাচন করুন", callback_data="select_country")],
        [InlineKeyboardButton("⬅️ ফিরে যান", callback_data="back_to_main")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """সাহায্য মেনু"""
    query = update.callback_query
    
    await query.answer()
    
    text = """
❓ **সাহায্য এবং নির্দেশনা**

**কিভাবে ব্যবহার করবেন:**

1️⃣ **দেশ নির্বাচন করুন** - আপনি যে দেশের নাম্বার চান তা নির্বাচন করুন
2️⃣ **প্ল্যাটফর্ম নির্বাচন করুন** - আপনি যে প্ল্যাটফর্মে অ্যাকাউন্ট খুলতে চান তা নির্বাচন করুন
3️⃣ **নাম্বার পান** - আমরা আপনাকে একটি সক্রিয় নাম্বার প্রদান করব
4️⃣ **কোড পান** - আপনার OTP আমাদের প্রাইভেট গ্রুপে পাঠানো হবে
5️⃣ **অ্যাকাউন্ট খুলুন** - প্রদত্ত নাম্বার দিয়ে আপনার অ্যাকাউন্ট খুলুন

**সমর্থিত প্ল্যাটফর্ম:**
📘 Facebook
💬 WhatsApp
📷 Instagram
🎵 TikTok
✈️ Telegram

**সমর্থিত দেশ:** {count} টি

⚠️ **গুরুত্বপূর্ণ নোট:**
- প্রতিটি নাম্বার শুধুমাত্র একবার ব্যবহার করা যায়
- OTP শুধুমাত্র সীমিত সময়ের জন্য বৈধ
- নাম্বার পরিবর্তন করতে "নাম্বার পরিবর্তন করুন" বাটন ক্লিক করুন
- সমস্ত OTP আমাদের প্রাইভেট গ্রুপে পাঠানো হয়

**যোগাযোগ করুন:**
আমাদের সাথে যোগাযোগ করতে @support_channel ভিজিট করুন
""".format(count=len(COUNTRIES))
    
    keyboard = [
        [InlineKeyboardButton("🏠 হোম", callback_data="back_to_main")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """মূল মেনুতে ফিরে যাওয়া"""
    query = update.callback_query
    
    await query.answer()
    
    text = """
🎯 **The hidden Sms Zone - মূল মেনু**

আপনি কি করতে চান?
"""
    
    keyboard = [
        [InlineKeyboardButton("🌍 দেশ নির্বাচন করুন", callback_data="select_country")],
        [InlineKeyboardButton("📊 সক্রিয় নাম্বার", callback_data="active_numbers")],
        [InlineKeyboardButton("❓ সাহায্য", callback_data="help")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """সমস্ত বাটন ক্লিক হ্যান্ডলার"""
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    
    await query.answer()
    
    # দেশ নির্বাচন
    if data.startswith("country_"):
        country_idx = int(data.split("_")[1]) - 1
        country_name = list(COUNTRIES.keys())[country_idx]
        
        if user_id not in user_data:
            user_data[user_id] = {}
        
        user_data[user_id]["country"] = country_name
        
        text = f"✅ **{country_name} নির্বাচিত হয়েছে**\n\nএখন প্ল্যাটফর্ম নির্বাচন করুন:"
        
        keyboard = [
            [InlineKeyboardButton(PLATFORMS["facebook"]["name"], callback_data="platform_facebook")],
            [InlineKeyboardButton(PLATFORMS["whatsapp"]["name"], callback_data="platform_whatsapp")],
            [InlineKeyboardButton(PLATFORMS["instagram"]["name"], callback_data="platform_instagram")],
            [InlineKeyboardButton(PLATFORMS["tiktok"]["name"], callback_data="platform_tiktok")],
            [InlineKeyboardButton(PLATFORMS["telegram"]["name"], callback_data="platform_telegram")],
            [InlineKeyboardButton("⬅️ ফিরে যান", callback_data="select_country")]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    
    # প্ল্যাটফর্ম নির্বাচন
    elif data.startswith("platform_"):
        platform_key = data.split("_")[1]
        platform_name = PLATFORMS[platform_key]["name"]
        
        if user_id not in user_data:
            user_data[user_id] = {}
        
        user_data[user_id]["platform"] = platform_name
        
        country_name = user_data[user_id].get("country", "অজানা")
        
        text = f"""
✅ **প্ল্যাটফর্ম নির্বাচিত হয়েছে**

🌍 **দেশ:** {country_name}
💻 **প্ল্যাটফর্ম:** {platform_name}

এখন আপনার নাম্বার পেতে নিচের বাটনে ক্লিক করুন:
"""
        
        keyboard = [
            [InlineKeyboardButton("📱 নাম্বার পান", callback_data="get_number")],
            [InlineKeyboardButton("🔀 প্ল্যাটফর্ম পরিবর্তন করুন", callback_data="select_platform")],
            [InlineKeyboardButton("⬅️ ফিরে যান", callback_data="select_country")]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    
    # নাম্বার পান
    elif data == "get_number":
        await show_number(update, context)
    
    # নাম্বার পরিবর্তন করুন
    elif data == "change_number":
        await change_number(update, context)
    
    # সক্রিয় নাম্বার
    elif data == "active_numbers":
        await active_numbers(update, context)
    
    # সাহায্য
    elif data == "help":
        await help_handler(update, context)
    
    # হোম
    elif data == "back_to_main":
        await back_to_main(update, context)
    
    # দেশ নির্বাচন
    elif data == "select_country":
        await select_country(update, context)
    
    # প্ল্যাটফর্ম নির্বাচন
    elif data == "select_platform":
        await select_platform(update, context)

def main() -> None:
    """বট শুরু করা"""
    # আপনার Telegram বট টোকেন এখানে রাখুন
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    # Application তৈরি করা
    application = Application.builder().token(TOKEN).build()
    
    # হ্যান্ডলার যোগ করা
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # বট শুরু করা
    application.run_polling()

if __name__ == '__main__':
    main()
