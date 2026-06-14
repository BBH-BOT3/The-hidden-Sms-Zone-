#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The hidden Sms Zone - ডেটা ম্যানেজার
নাম্বার এবং ব্যবহারকারী ডেটা পরিচালনা করার জন্য
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class DataManager:
    """ডেটা পরিচালনা ক্লাস"""
    
    def __init__(self, data_file: str = "bot_data.json"):
        self.data_file = data_file
        self.data = self.load_data()
    
    def load_data(self) -> Dict:
        """ডেটা ফাইল থেকে লোড করা"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"ডেটা লোড করতে ত্রুটি: {e}")
                return self.get_default_data()
        return self.get_default_data()
    
    def get_default_data(self) -> Dict:
        """ডিফল্ট ডেটা স্ট্রাকচার"""
        return {
            "users": {},
            "numbers": {},
            "statistics": {
                "total_users": 0,
                "total_requests": 0,
                "created_date": datetime.now().isoformat()
            }
        }
    
    def save_data(self) -> bool:
        """ডেটা ফাইলে সংরক্ষণ করা"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"ডেটা সংরক্ষণ করতে ত্রুটি: {e}")
            return False
    
    def add_user(self, user_id: int, user_name: str) -> bool:
        """নতুন ব্যবহারকারী যোগ করা"""
        if user_id not in self.data["users"]:
            self.data["users"][str(user_id)] = {
                "name": user_name,
                "joined_date": datetime.now().isoformat(),
                "requests": 0,
                "last_country": None,
                "last_platform": None
            }
            self.data["statistics"]["total_users"] += 1
            return self.save_data()
        return False
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """ব্যবহারকারী তথ্য পান"""
        return self.data["users"].get(str(user_id))
    
    def update_user_request(self, user_id: int, country: str, platform: str) -> bool:
        """ব্যবহারকারীর অনুরোধ আপডেট করা"""
        if str(user_id) in self.data["users"]:
            self.data["users"][str(user_id)]["requests"] += 1
            self.data["users"][str(user_id)]["last_country"] = country
            self.data["users"][str(user_id)]["last_platform"] = platform
            self.data["statistics"]["total_requests"] += 1
            return self.save_data()
        return False
    
    def get_statistics(self) -> Dict:
        """পরিসংখ্যান পান"""
        return self.data["statistics"]
    
    def export_data(self, export_file: str = "bot_data_export.json") -> bool:
        """ডেটা এক্সপোর্ট করা"""
        try:
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"ডেটা এক্সপোর্ট করতে ত্রুটি: {e}")
            return False
    
    def get_user_count(self) -> int:
        """মোট ব্যবহারকারী সংখ্যা"""
        return len(self.data["users"])
    
    def get_total_requests(self) -> int:
        """মোট অনুরোধ সংখ্যা"""
        return self.data["statistics"]["total_requests"]


class NumberManager:
    """নাম্বার পরিচালনা ক্লাস"""
    
    def __init__(self):
        self.numbers_file = "numbers.json"
        self.numbers = self.load_numbers()
    
    def load_numbers(self) -> Dict:
        """নাম্বার ফাইল থেকে লোড করা"""
        if os.path.exists(self.numbers_file):
            try:
                with open(self.numbers_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"নাম্বার লোড করতে ত্রুটি: {e}")
                return {}
        return {}
    
    def save_numbers(self) -> bool:
        """নাম্বার ফাইলে সংরক্ষণ করা"""
        try:
            with open(self.numbers_file, 'w', encoding='utf-8') as f:
                json.dump(self.numbers, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"নাম্বার সংরক্ষণ করতে ত্রুটি: {e}")
            return False
    
    def add_number(self, country: str, platform: str, number: str, otp: str) -> bool:
        """নাম্বার যোগ করা"""
        key = f"{country}_{platform}"
        if key not in self.numbers:
            self.numbers[key] = []
        
        self.numbers[key].append({
            "number": number,
            "otp": otp,
            "created_date": datetime.now().isoformat(),
            "used": False
        })
        return self.save_numbers()
    
    def mark_number_used(self, country: str, platform: str, number: str) -> bool:
        """নাম্বার ব্যবহৃত হিসেবে চিহ্নিত করা"""
        key = f"{country}_{platform}"
        if key in self.numbers:
            for num_obj in self.numbers[key]:
                if num_obj["number"] == number:
                    num_obj["used"] = True
                    return self.save_numbers()
        return False
    
    def get_available_numbers(self, country: str, platform: str) -> List[Dict]:
        """উপলব্ধ নাম্বার পান"""
        key = f"{country}_{platform}"
        if key in self.numbers:
            return [n for n in self.numbers[key] if not n["used"]]
        return []
    
    def get_statistics(self) -> Dict:
        """নাম্বার পরিসংখ্যান"""
        total = 0
        used = 0
        available = 0
        
        for key in self.numbers:
            for num_obj in self.numbers[key]:
                total += 1
                if num_obj["used"]:
                    used += 1
                else:
                    available += 1
        
        return {
            "total": total,
            "used": used,
            "available": available
        }


class LogManager:
    """লগ পরিচালনা ক্লাস"""
    
    def __init__(self, log_file: str = "bot.log"):
        self.log_file = log_file
    
    def log(self, level: str, message: str) -> None:
        """লগ করা"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_message)
        except Exception as e:
            print(f"লগ করতে ত্রুটি: {e}")
    
    def log_info(self, message: str) -> None:
        """তথ্য লগ করা"""
        self.log("INFO", message)
    
    def log_error(self, message: str) -> None:
        """ত্রুটি লগ করা"""
        self.log("ERROR", message)
    
    def log_warning(self, message: str) -> None:
        """সতর্কতা লগ করা"""
        self.log("WARNING", message)
    
    def log_debug(self, message: str) -> None:
        """ডিবাগ লগ করা"""
        self.log("DEBUG", message)
    
    def clear_log(self) -> bool:
        """লগ ফাইল পরিষ্কার করা"""
        try:
            open(self.log_file, 'w').close()
            return True
        except Exception as e:
            print(f"লগ পরিষ্কার করতে ত্রুটি: {e}")
            return False
    
    def get_log_size(self) -> int:
        """লগ ফাইলের আকার পান (বাইটে)"""
        if os.path.exists(self.log_file):
            return os.path.getsize(self.log_file)
        return 0


# ব্যবহারের উদাহরণ
if __name__ == "__main__":
    # ডেটা ম্যানেজার ব্যবহার
    dm = DataManager()
    dm.add_user(123456, "Test User")
    dm.update_user_request(123456, "Bangladesh", "WhatsApp")
    print("ব্যবহারকারী পরিসংখ্যান:", dm.get_statistics())
    
    # নাম্বার ম্যানেজার ব্যবহার
    nm = NumberManager()
    nm.add_number("Bangladesh", "WhatsApp", "+8801700000001", "123456")
    print("নাম্বার পরিসংখ্যান:", nm.get_statistics())
    
    # লগ ম্যানেজার ব্যবহার
    lm = LogManager()
    lm.log_info("বট শুরু হয়েছে")
    lm.log_error("একটি ত্রুটি ঘটেছে")
