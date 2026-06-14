#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The hidden Sms Zone - নাম্বার ডেটা সেটআপ স্ক্রিপ্ট
এই স্ক্রিপ্ট সমস্ত দেশ এবং প্ল্যাটফর্মের জন্য নাম্বার তৈরি করে
"""

import json
import random
from datetime import datetime
from data_manager import NumberManager

# দেশ এবং তাদের কোড
COUNTRIES_DATA = {
    "Bangladesh": {
        "code": "+880",
        "flag": "🇧🇩",
        "prefixes": ["1700", "1800", "1900"]
    },
    "India": {
        "code": "+91",
        "flag": "🇮🇳",
        "prefixes": ["9000", "9100", "9200", "9300", "9400"]
    },
    "Pakistan": {
        "code": "+92",
        "flag": "🇵🇰",
        "prefixes": ["3000", "3100", "3200", "3300", "3400"]
    },
    "Zambia": {
        "code": "+260",
        "flag": "🇿🇲",
        "prefixes": ["755", "765", "770"]
    },
    "Uganda": {
        "code": "+256",
        "flag": "🇺🇬",
        "prefixes": ["700", "750", "760"]
    },
    "Kenya": {
        "code": "+254",
        "flag": "🇰🇪",
        "prefixes": ["700", "710", "720", "730", "740"]
    },
    "Ghana": {
        "code": "+233",
        "flag": "🇬🇭",
        "prefixes": ["500", "510", "520", "530", "540"]
    },
    "Nigeria": {
        "code": "+234",
        "flag": "🇳🇬",
        "prefixes": ["800", "810", "820", "830", "840"]
    },
    "Ethiopia": {
        "code": "+251",
        "flag": "🇪🇹",
        "prefixes": ["900", "910", "920", "930", "940"]
    },
    "Mozambique": {
        "code": "+258",
        "flag": "🇲🇿",
        "prefixes": ["840", "850", "860", "870", "880"]
    }
}

PLATFORMS = ["Facebook", "WhatsApp", "Instagram", "TikTok", "Telegram"]

def generate_phone_number(country_code: str, prefix: str) -> str:
    """ফোন নাম্বার জেনারেট করা"""
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return f"{country_code}{prefix}{random_digits}"

def generate_otp() -> str:
    """OTP জেনারেট করা"""
    return str(random.randint(100000, 999999))

def setup_numbers(numbers_per_combination: int = 15) -> None:
    """সমস্ত নাম্বার ডেটা সেটআপ করা"""
    
    nm = NumberManager()
    total_numbers = 0
    
    print("🚀 নাম্বার ডেটা সেটআপ শুরু হচ্ছে...\n")
    
    for country, country_info in COUNTRIES_DATA.items():
        country_code = country_info["code"]
        prefixes = country_info["prefixes"]
        
        print(f"📍 {country_info['flag']} {country} এর জন্য নাম্বার তৈরি করছি...")
        
        for platform in PLATFORMS:
            numbers_created = 0
            
            # প্রতিটি কম্বিনেশনের জন্য নাম্বার তৈরি করা
            for _ in range(numbers_per_combination):
                prefix = random.choice(prefixes)
                phone_number = generate_phone_number(country_code, prefix)
                otp = generate_otp()
                
                nm.add_number(country, platform, phone_number, otp)
                numbers_created += 1
                total_numbers += 1
            
            print(f"  ✓ {platform}: {numbers_created} নাম্বার তৈরি করা হয়েছে")
        
        print()
    
    print("=" * 50)
    print(f"✅ সেটআপ সম্পন্ন!")
    print(f"📊 মোট নাম্বার তৈরি করা হয়েছে: {total_numbers}")
    print(f"📍 মোট দেশ: {len(COUNTRIES_DATA)}")
    print(f"💻 মোট প্ল্যাটফর্ম: {len(PLATFORMS)}")
    print(f"📈 সম্ভাব্য সংমিশ্রণ: {len(COUNTRIES_DATA) * len(PLATFORMS)}")
    print("=" * 50)

def export_numbers_report() -> None:
    """নাম্বার রিপোর্ট এক্সপোর্ট করা"""
    
    nm = NumberManager()
    stats = nm.get_statistics()
    
    report = f"""
╔════════════════════════════════════════╗
║   The hidden Sms Zone - নাম্বার রিপোর্ট   ║
╚════════════════════════════════════════╝

📊 পরিসংখ্যান:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  • মোট নাম্বার: {stats['total']}
  • ব্যবহৃত নাম্বার: {stats['used']}
  • উপলব্ধ নাম্বার: {stats['available']}

📍 দেশ সমূহ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for idx, country in enumerate(COUNTRIES_DATA.keys(), 1):
        report += f"  {idx}. {COUNTRIES_DATA[country]['flag']} {country}\n"
    
    report += f"""
💻 প্ল্যাটফর্ম সমূহ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for idx, platform in enumerate(PLATFORMS, 1):
        report += f"  {idx}. {platform}\n"
    
    report += f"""
⏰ তৈরির সময়: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    print(report)
    
    # রিপোর্ট ফাইলে সংরক্ষণ করা
    with open("numbers_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("✅ রিপোর্ট 'numbers_report.txt' ফাইলে সংরক্ষণ করা হয়েছে")

if __name__ == "__main__":
    import sys
    
    print("""
╔════════════════════════════════════════╗
║  The hidden Sms Zone - সেটআপ স্ক্রিপ্ট    ║
╚════════════════════════════════════════╝
""")
    
    # কমান্ড লাইন আর্গুমেন্ট চেক করা
    if len(sys.argv) > 1:
        if sys.argv[1] == "--setup":
            # নাম্বার সেটআপ করা
            numbers_per_combo = 15
            if len(sys.argv) > 2:
                try:
                    numbers_per_combo = int(sys.argv[2])
                except ValueError:
                    print("❌ অবৈধ সংখ্যা। ডিফল্ট ১৫ ব্যবহার করা হচ্ছে।")
            
            setup_numbers(numbers_per_combo)
            export_numbers_report()
        
        elif sys.argv[1] == "--report":
            # শুধুমাত্র রিপোর্ট দেখানো
            export_numbers_report()
        
        elif sys.argv[1] == "--help":
            print("""
ব্যবহার:
  python setup_numbers.py [বিকল্প] [প্যারামিটার]

বিকল্প:
  --setup [সংখ্যা]    নাম্বার সেটআপ করুন (ডিফল্ট: ১৫ প্রতি কম্বিনেশন)
  --report             নাম্বার রিপোর্ট দেখান
  --help               এই সাহায্য বার্তা দেখান

উদাহরণ:
  python setup_numbers.py --setup         # ডিফল্ট সেটআপ
  python setup_numbers.py --setup 20      # ২০ নাম্বার প্রতি কম্বিনেশন
  python setup_numbers.py --report        # রিপোর্ট দেখান
""")
        else:
            print("❌ অজানা বিকল্প। সাহায্যের জন্য --help ব্যবহার করুন।")
    else:
        # ডিফল্ট সেটআপ
        setup_numbers()
        export_numbers_report()
