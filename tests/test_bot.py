import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from thaichatbot.bot import ThaiChatBot

def test_reply():
    print("เริ่มสร้างบอท")
    bot = ThaiChatBot("ทดสอบบอท")
    print("สร้างบอทเสร็จ")

    r1 = bot.reply("สวัสดี")
    print("ตอบสวัสดี:", r1)
    assert r1.startswith("สวัสดี")

    r2 = bot.reply("ชื่ออะไร")
    print("ตอบชื่ออะไร:", r2)
    assert "ทดสอบบอท" in r2

     # เช็คว่า reply อากาศไม่ใช่ข้อความแปลก ๆ หรือเช็คคำหลัก
    r3 = bot.reply("อากาศเป็นยังไง")
    print("ตอบอากาศเป็นยังไง:", r3)
    assert "อากาศ" in r3 or "แจ่มใส" in r3 or "ไม่เข้าใจ" in r3  # หรือเช็คคำอื่นที่คาดว่าอาจตอบ
    

