@echo off
REM The hidden Sms Zone - বট চালানোর স্ক্রিপ্ট (Windows)

echo ================================
echo The hidden Sms Zone - বট শুরু হচ্ছে
echo ================================
echo.

REM Python সংস্করণ চেক করা
echo ✓ Python সংস্করণ চেক করছি...
python --version

REM প্রয়োজনীয় প্যাকেজ ইনস্টল করা
echo.
echo ✓ প্রয়োজনীয় প্যাকেজ ইনস্টল করছি...
pip install -r requirements.txt

REM বট টোকেন চেক করা
echo.
echo ✓ বট কনফিগারেশন চেক করছি...

findstr /M "YOUR_BOT_TOKEN_HERE" the_hidden_sms_zone_bot.py
if %errorlevel% equ 0 (
    echo.
    echo ⚠️  সতর্কতা: বট টোকেন সেট করা হয়নি!
    echo.
    echo দয়া করে নিম্নলিখিত ধাপ অনুসরণ করুন:
    echo 1. the_hidden_sms_zone_bot.py ফাইলটি খুলুন
    echo 2. 'YOUR_BOT_TOKEN_HERE' খুঁজুন
    echo 3. আপনার বট টোকেন দিয়ে প্রতিস্থাপন করুন
    echo 4. ফাইলটি সংরক্ষণ করুন
    echo 5. এই স্ক্রিপ্টটি আবার চালান
    echo.
    pause
    exit /b 1
)

REM বট শুরু করা
echo.
echo ================================
echo ✓ বট এখন চলছে...
echo ================================
echo.
echo Telegram এ আপনার বট খুঁজুন এবং /start পাঠান
echo.
echo বট বন্ধ করতে Ctrl+C চাপুন
echo.

python the_hidden_sms_zone_bot.py

pause
