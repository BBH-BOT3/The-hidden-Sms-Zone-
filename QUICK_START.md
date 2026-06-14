# ⚡ দ্রুত শুরু (৫ মিনিটে)

এই গাইডটি শুধুমাত্র দ্রুত সেটআপের জন্য। বিস্তারিত জানতে `COMPLETE_SETUP_BENGALI.md` পড়ুন।

---

## 🎯 মাত্র ৫ ধাপ

### ধাপ ১: বট টোকেন পান (২ মিনিট)

```
Telegram → @BotFather → /newbot
নাম: The hidden Sms Zone
ইউজারনেম: hidden_sms_zone_bot
টোকেন কপি করুন ✅
```

**উদাহরণ:**
```
123456789:ABCdefGHIjklmnoPQRstuvwxyzABCDEFGH
```

---

### ধাপ ২: গ্রুপ তৈরি করুন (১ মিনিট)

```
Telegram → নতুন গ্রুপ
নাম: The hidden Sms Zone - OTP Codes
প্রাইভেট করুন
@userinfobot যোগ করুন
Group ID কপি করুন ✅
```

**উদাহরণ:**
```
-1001234567890
```

---

### ধাপ ৩: ফাইল ডাউনলোড এবং এক্সট্র্যাক্ট করুন (১ মিনিট)

```
the_hidden_sms_zone_v2_complete.tar.gz ডাউনলোড করুন
এক্সট্র্যাক্ট করুন
ফোল্ডার খুলুন
```

---

### ধাপ ৪: কোড এডিট করুন (১ মিনিট)

`the_hidden_sms_zone_bot_v2.py` খুলুন এবং এই দুটি লাইন পরিবর্তন করুন:

**লাইন ১৫:**
```python
ADMIN_GROUP_ID = -1001234567890  # আপনার গ্রুপ ID
```

**লাইন ১০৫:**
```python
TOKEN = "123456789:ABCdefGHIjklmnoPQRstuvwxyzABCDEFGH"  # আপনার বট টোকেন
```

সংরক্ষণ করুন (Ctrl+S)

---

### ধাপ ৫: চালান (অবিলম্বে)

কমান্ড প্রম্পট/টার্মিনাল খুলুন:

```bash
cd ফোল্ডারের_পাথ
pip install -r requirements.txt
python the_hidden_sms_zone_bot_v2.py
```

---

## ✅ টেস্ট করুন

```
Telegram → আপনার বট খুঁজুন
/start পাঠান
দেশ নির্বাচন করুন
প্ল্যাটফর্ম নির্বাচন করুন
"নাম্বার পান" ক্লিক করুন
গ্রুপে OTP দেখুন ✅
```

---

## 🎉 সম্পন্ন!

আপনার বট এখন চলছে! 🚀

---

## 📞 সমস্যা?

| সমস্যা | সমাধান |
|--------|--------|
| "ModuleNotFoundError" | `pip install python-telegram-bot` |
| "Invalid token" | টোকেন সঠিক কিনা চেক করুন |
| "বট সাড়া দিচ্ছে না" | ইন্টারনেট চেক করুন, বট পুনরায় চালান |
| "গ্রুপে মেসেজ নেই" | গ্রুপ ID সঠিক কিনা চেক করুন |

---

**বিস্তারিত সাহায্যের জন্য `COMPLETE_SETUP_BENGALI.md` পড়ুন।**
