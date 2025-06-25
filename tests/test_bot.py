# tests/test_bot.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from thaichatbot.bot import ThaiChatBot

def test_reply():
    bot = ThaiChatBot("ทดสอบบอท")
    assert bot.reply("สวัสดี").startswith("สวัสดี")
    assert "ทดสอบบอท" in bot.reply("ชื่ออะไร")
    assert "ไม่เข้าใจ" in bot.reply("อากาศเป็นยังไง")  # ไม่รู้เรื่อง
