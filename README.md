# 🎯 The hidden Sms Zone - Telegram Bot

একটি সম্পূর্ণ এবং পেশাদার Telegram বট যা ব্যবহারকারীদের বিভিন্ন দেশের ভার্চুয়াল নাম্বার প্রদান করে এবং তারা সেই নাম্বারগুলি দিয়ে সোশ্যাল মিডিয়া অ্যাকাউন্ট খুলতে পারে।

---

## 📋 বৈশিষ্ট্য

### 🌍 ১০টি দেশ সাপোর্ট
- 🇧🇩 Bangladesh
- 🇮🇳 India
- 🇵🇰 Pakistan
- 🇿🇲 Zambia
- 🇺🇬 Uganda
- 🇰🇪 Kenya
- 🇬🇭 Ghana
- 🇳🇬 Nigeria
- 🇪🇹 Ethiopia
- 🇲🇿 Mozambique

### 💻 ৫টি প্ল্যাটফর্ম সাপোর্ট
- 📘 Facebook
- 💬 WhatsApp
- 📷 Instagram
- 🎵 TikTok
- ✈️ Telegram

### ⚙️ মূল ফিচার
- ✅ দেশ নির্বাচন মেনু
- ✅ প্ল্যাটফর্ম নির্বাচন মেনু
- ✅ র্যান্ডম নাম্বার জেনারেশন
- ✅ ৬ ডিজিটের OTP জেনারেশন
- ✅ নাম্বার পরিবর্তন ফিচার
- ✅ প্ল্যাটফর্ম পরিবর্তন ফিচার
- ✅ সক্রিয় নাম্বার তালিকা
- ✅ বিস্তারিত সাহায্য মেনু
- ✅ ব্যবহারকারী ডেটা ট্র্যাকিং
- ✅ পরিসংখ্যান এবং রিপোর্টিং

---

## 🚀 দ্রুত শুরু

### প্রয়োজনীয়তা
- Python 3.8 বা তার উপরে
- pip (Python প্যাকেজ ম্যানেজার)
- Telegram অ্যাকাউন্ট
- ইন্টারনেট সংযোগ

### ইনস্টলেশন

1. **রিপোজিটরি ক্লোন করুন বা ফাইলগুলি ডাউনলোড করুন**
```bash
git clone https://github.com/yourusername/the-hidden-sms-zone.git
cd the-hidden-sms-zone
```

2. **প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**
```bash
pip install -r requirements.txt
```

3. **Telegram বট টোকেন পান**
   - Telegram এ @BotFather খুঁজুন
   - `/newbot` কমান্ড পাঠান
   - বটের নাম এবং ইউজারনেম দিন
   - টোকেন কপি করুন

4. **বট টোকেন কনফিগার করুন**
   - `the_hidden_sms_zone_bot.py` খুলুন
   - `TOKEN = "YOUR_BOT_TOKEN_HERE"` খুঁজুন
   - আপনার টোকেন দিয়ে প্রতিস্থাপন করুন

5. **বট চালান**
```bash
# Linux/Mac
bash run_bot.sh

# Windows
run_bot.bat

# অথবা সরাসরি
python the_hidden_sms_zone_bot.py
```

---

## 📁 ফাইল কাঠামো

```
the-hidden-sms-zone/
├── the_hidden_sms_zone_bot.py    # মূল বট কোড
├── data_manager.py               # ডেটা পরিচালনা মডিউল
├── config.json                   # কনফিগারেশন ফাইল
├── requirements.txt              # প্রয়োজনীয় প্যাকেজ
├── run_bot.sh                    # Linux/Mac চালানোর স্ক্রিপ্ট
├── run_bot.bat                   # Windows চালানোর স্ক্রিপ্ট
├── README.md                     # এই ফাইল
├── SETUP_GUIDE_BENGALI.md        # বিস্তারিত সেটআপ গাইড
└── bot_data.json                 # ব্যবহারকারী ডেটা (স্বয়ংক্রিয় তৈরি)
```

---

## 🎮 ব্যবহার

### ব্যবহারকারীর জন্য

1. Telegram এ আপনার বট খুঁজুন
2. `/start` কমান্ড পাঠান
3. **দেশ নির্বাচন করুন**
4. **প্ল্যাটফর্ম নির্বাচন করুন**
5. **নাম্বার পান**
6. **প্রদত্ত নাম্বার এবং OTP দিয়ে অ্যাকাউন্ট খুলুন**

### উপলব্ধ কমান্ড

| কমান্ড | বর্ণনা |
|--------|--------|
| `/start` | বট শুরু করুন এবং স্বাগত বার্তা পান |
| `/help` | সাহায্য এবং নির্দেশনা পান |
| `/stats` | আপনার পরিসংখ্যান দেখুন |
| `/countries` | সমর্থিত দেশের তালিকা দেখুন |
| `/platforms` | সমর্থিত প্ল্যাটফর্মের তালিকা দেখুন |

---

## 🔧 কাস্টমাইজেশন

### নতুন দেশ যোগ করা

`the_hidden_sms_zone_bot.py` ফাইলে `COUNTRIES` ডিকশনারি খুঁজুন এবং যোগ করুন:

```python
"🇧🇷 Brazil": {
    "code": "+55",
    "flag": "🇧🇷",
    "numbers": [
        "+5511999999999",
        "+5511999999998",
        # আরও নাম্বার...
    ]
}
```

### নতুন প্ল্যাটফর্ম যোগ করা

`PLATFORMS` ডিকশনারিতে যোগ করুন:

```python
"twitter": {"name": "𝕏 Twitter", "emoji": "𝕏"}
```

### বার্তা কাস্টমাইজ করা

`config.json` ফাইলে `messages` সেকশন সম্পাদনা করুন।

---

## 📊 ডেটা ম্যানেজমেন্ট

### ডেটা ম্যানেজার ব্যবহার করা

```python
from data_manager import DataManager, NumberManager, LogManager

# ব্যবহারকারী ডেটা
dm = DataManager()
dm.add_user(123456, "User Name")
dm.update_user_request(123456, "Bangladesh", "WhatsApp")

# নাম্বার ম্যানেজমেন্ট
nm = NumberManager()
nm.add_number("Bangladesh", "WhatsApp", "+8801700000001", "123456")

# লগিং
lm = LogManager()
lm.log_info("বট শুরু হয়েছে")
```

---

## 🐛 সমস্যা সমাধান

### সমস্যা: "ModuleNotFoundError: No module named 'telegram'"

**সমাধান:**
```bash
pip install python-telegram-bot
```

### সমস্যা: "Invalid token" ত্রুটি

**সমাধান:**
- টোকেন সঠিক কিনা চেক করুন
- @BotFather থেকে নতুন টোকেন তৈরি করুন
- কোডে টোকেন সঠিকভাবে রাখা আছে কিনা দেখুন

### সমস্যা: বট সাড়া দিচ্ছে না

**সমাধান:**
- ইন্টারনেট সংযোগ চেক করুন
- বট চলছে কিনা টার্মিনালে দেখুন
- বটকে পুনরায় চালু করুন

### সমস্যা: "Connection error"

**সমাধান:**
- ফায়ারওয়াল সেটিংস চেক করুন
- VPN ব্যবহার করে দেখুন
- ইন্টারনেট সংযোগ পুনরায় চেষ্টা করুন

---

## 📈 পরিসংখ্যান

- **মোট দেশ:** ১০টি
- **প্রতিটি দেশে নাম্বার:** ১২টি
- **মোট নাম্বার:** ১২০টি
- **সমর্থিত প্ল্যাটফর্ম:** ৫টি
- **সম্ভাব্য সংমিশ্রণ:** ৬০০টি

---

## 🔐 নিরাপত্তা

⚠️ **গুরুত্বপূর্ণ নিরাপত্তা টিপস:**

1. **টোকেন সুরক্ষিত রাখুন** - কখনও কাউকে আপনার বট টোকেন দেবেন না
2. **সংবেদনশীল তথ্য শেয়ার করবেন না** - বটে ব্যক্তিগত তথ্য সংরক্ষণ করবেন না
3. **নিয়মিত আপডেট করুন** - python-telegram-bot এর নতুন সংস্করণ ব্যবহার করুন
4. **লগ ফাইল পরিষ্কার করুন** - নিয়মিত লগ ফাইল পরিষ্কার করুন
5. **ডেটা ব্যাকআপ করুন** - নিয়মিত ডেটা ব্যাকআপ নিন

---

## 📝 লাইসেন্স

এই প্রজেক্টটি MIT লাইসেন্সের অধীন। বিস্তারিত জানতে `LICENSE` ফাইল দেখুন।

---

## 🤝 অবদান রাখুন

আপনার অবদান স্বাগত জানাই! অনুগ্রহ করে:

1. প্রজেক্টটি ফোর্ক করুন
2. একটি নতুন ব্র্যাঞ্চ তৈরি করুন (`git checkout -b feature/AmazingFeature`)
3. আপনার পরিবর্তন কমিট করুন (`git commit -m 'Add some AmazingFeature'`)
4. ব্র্যাঞ্চে পুশ করুন (`git push origin feature/AmazingFeature`)
5. একটি Pull Request খুলুন

---

## 📞 যোগাযোগ

যদি কোনো প্রশ্ন বা পরামর্শ থাকে:

- 📧 ইমেইল: support@example.com
- 💬 Telegram: @support_channel
- 🐛 GitHub Issues: [GitHub Issues](https://github.com/yourusername/the-hidden-sms-zone/issues)

---

## 🎉 ধন্যবাদ!

এই বটটি ব্যবহার করার জন্য ধন্যবাদ। আমরা আশা করি এটি আপনার জন্য উপকারী হবে।

**সুখী বটিং! 🚀**

---

## 📚 সম্পর্কিত রিসোর্স

- [python-telegram-bot ডকুমেন্টেশন](https://python-telegram-bot.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather টিউটোরিয়াল](https://core.telegram.org/bots#botfather)

---

**সংস্করণ:** 1.0.0  
**শেষ আপডেট:** 2026-06-14  
**লেখক:** The hidden Sms Zone Team
