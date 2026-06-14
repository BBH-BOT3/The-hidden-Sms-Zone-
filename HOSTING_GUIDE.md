# 🌐 The hidden Sms Zone - যেকোনো জায়গায় হোস্ট করার গাইড

আপনার বট ২৪/৭ চালু রাখতে যেকোনো জায়গায় হোস্ট করতে পারেন। এখানে সেরা বিকল্পগুলি দেখানো হয়েছে।

---

## 🎯 হোস্টিং অপশন তুলনা

| প্ল্যাটফর্ম | খরচ | সেটআপ | পারফরম্যান্স | সুপারিশ |
|-----------|------|--------|------------|---------|
| **Railway.app** | ✅ ফ্রি | ⭐⭐⭐ | ⭐⭐⭐⭐ | 🏆 সেরা |
| **Render** | ✅ ফ্রি | ⭐⭐⭐ | ⭐⭐⭐ | ✅ ভালো |
| **PythonAnywhere** | ✅ ফ্রি | ⭐⭐ | ⭐⭐ | সীমিত |
| **Replit** | ✅ ফ্রি | ⭐⭐⭐⭐ | ⭐⭐ | শুরুর জন্য |
| **AWS/GCP** | ⚠️ ফ্রি (১ বছর) | ⭐ | ⭐⭐⭐⭐⭐ | শক্তিশালী |
| **আপনার কম্পিউটার** | ✅ ফ্রি | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | সহজ |

---

## 🚀 অপশন ১: আপনার নিজের কম্পিউটারে (সহজতম)

### সুবিধা:
✅ সম্পূর্ণ ফ্রি
✅ সেটআপ সহজ
✅ সম্পূর্ণ নিয়ন্ত্রণ
✅ কোন সীমাবদ্ধতা নেই

### অসুবিধা:
❌ কম্পিউটার চালু রাখতে হবে
❌ ইন্টারনেট সংযোগ প্রয়োজন
❌ বিদ্যুৎ খরচ

### সেটআপ:

```bash
# ১. প্যাকেজ ইনস্টল করুন
pip install -r requirements.txt

# ২. বট টোকেন এবং গ্রুপ ID সেট করুন
# the_hidden_sms_zone_bot_v2.py খুলুন এবং সেট করুন

# ৩. বট চালান
python the_hidden_sms_zone_bot_v2.py
```

---

## 🚀 অপশন ২: Railway.app (সুপারিশকৃত)

Railway.app হল সবচেয়ে সহজ এবং নির্ভরযোগ্য ফ্রি হোস্টিং।

### ধাপ ১: Railway.app এ সাইন আপ করুন

1. https://railway.app এ যান
2. GitHub দিয়ে সাইন আপ করুন (সহজ)
3. একটি নতুন প্রজেক্ট তৈরি করুন

### ধাপ ২: GitHub এ রিপোজিটরি তৈরি করুন

1. https://github.com/new এ যান
2. রিপোজিটরি নাম: `the-hidden-sms-zone`
3. "Create repository" ক্লিক করুন

### ধাপ ৩: ফাইল আপলোড করুন

```bash
# আপনার কম্পিউটারে
git clone https://github.com/YOUR_USERNAME/the-hidden-sms-zone.git
cd the-hidden-sms-zone

# সমস্ত ফাইল কপি করুন এই ফোল্ডারে
# তারপর:
git add .
git commit -m "Initial commit"
git push origin main
```

### ধাপ ৪: Railway এ ডিপ্লয় করুন

1. Railway.app এ লগইন করুন
2. "New Project" → "Deploy from GitHub"
3. আপনার রিপোজিটরি নির্বাচন করুন
4. "Deploy" ক্লিক করুন

### ধাপ ৫: পরিবেশ ভেরিয়েবল সেট করুন

Railway ড্যাশবোর্ডে:

1. "Variables" ট্যাব খুলুন
2. নতুন ভেরিয়েবল যোগ করুন:

```
BOT_TOKEN = আপনার_বট_টোকেন
ADMIN_GROUP_ID = আপনার_গ্রুপ_আইডি
```

---

## 🚀 অপশন ৩: Render

### ধাপ ১: Render.com এ সাইন আপ করুন

1. https://render.com এ যান
2. GitHub দিয়ে সাইন আপ করুন

### ধাপ ২: নতুন সার্ভিস তৈরি করুন

1. "New +" → "Web Service"
2. GitHub রিপোজিটরি সংযুক্ত করুন
3. নাম: `the-hidden-sms-zone`
4. Runtime: `Python 3`

### ধাপ ৩: কনফিগার করুন

```
Build Command: pip install -r requirements.txt
Start Command: python the_hidden_sms_zone_bot_v2.py
```

### ধাপ ৪: পরিবেশ ভেরিয়েবল যোগ করুন

```
BOT_TOKEN = আপনার_বট_টোকেন
ADMIN_GROUP_ID = আপনার_গ্রুপ_আইডি
```

---

## 🚀 অপশন ৪: PythonAnywhere

### ধাপ ১: PythonAnywhere এ সাইন আপ করুন

1. https://www.pythonanywhere.com এ যান
2. ফ্রি অ্যাকাউন্ট তৈরি করুন

### ধাপ ২: Bash কনসোল খুলুন

1. "Consoles" → "Bash"
2. ফাইল আপলোড করুন:

```bash
git clone https://github.com/YOUR_USERNAME/the-hidden-sms-zone.git
cd the-hidden-sms-zone
pip install -r requirements.txt
```

### ধাপ ৩: Scheduled Task তৈরি করুন

1. "Web" → "Add a new web app"
2. "Tasks" → "Add a new scheduled task"
3. সময়: প্রতিদিন
4. কমান্ড: `python /home/username/the-hidden-sms-zone/the_hidden_sms_zone_bot_v2.py`

---

## 🚀 অপশন ৫: Replit

### ধাপ ১: Replit এ সাইন আপ করুন

1. https://replit.com এ যান
2. GitHub দিয়ে সাইন আপ করুন

### ধাপ ২: নতুন Repl তৈরি করুন

1. "Create" ক্লিক করুন
2. "Import from GitHub"
3. আপনার রিপোজিটরি URL পেস্ট করুন

### ধাপ ৩: চালান

1. "Run" বাটন ক্লিক করুন
2. বট শুরু হবে

### ধাপ ৪: ২৪/৭ রাখতে

Replit Boosts কিনুন (বা ফ্রি ভার্সন ১৫ মিনিট পর পর বন্ধ হয়)

---

## 🐳 অপশন ৬: Docker ব্যবহার করে

যেকোনো জায়গায় Docker দিয়ে হোস্ট করুন।

### Dockerfile তৈরি করুন:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "the_hidden_sms_zone_bot_v2.py"]
```

### Docker চালান:

```bash
# ইমেজ তৈরি করুন
docker build -t sms-zone-bot .

# কন্টেইনার চালান
docker run -e BOT_TOKEN="YOUR_TOKEN" \
           -e ADMIN_GROUP_ID="YOUR_GROUP_ID" \
           sms-zone-bot
```

---

## 📋 সেটআপ চেকলিস্ট

### প্রতিটি হোস্টিং এর জন্য প্রয়োজনীয়:

- [ ] **BOT_TOKEN** সেট করা
- [ ] **ADMIN_GROUP_ID** সেট করা
- [ ] **requirements.txt** আপলোড করা
- [ ] **the_hidden_sms_zone_bot_v2.py** আপলোড করা
- [ ] Python 3.8+ ইনস্টল করা
- [ ] বট চালু করা
- [ ] টেস্ট করা

---

## 🧪 সব জায়গায় একই কোড

আপনার বট কোড সব জায়গায় একই থাকবে। শুধু এনভায়রনমেন্ট ভেরিয়েবল পরিবর্তন করুন।

### পরিবেশ ভেরিয়েবল ব্যবহার করার জন্য কোড আপডেট করুন:

```python
import os

TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID", "-1001234567890"))
```

---

## 💡 সুপারিশ

**শুরুর জন্য:** Railway.app বা Render
**দীর্ঘমেয়াদে:** আপনার নিজের সার্ভার বা AWS
**সবচেয়ে সহজ:** আপনার কম্পিউটার

---

## 🎉 সম্পন্ন!

এখন আপনার বট যেকোনো জায়গায় ২৪/৭ চলবে এবং সমস্ত OTP কোড আপনার গ্রুপে পাঠাবে।

**সুখী বটিং! 🚀**
