# tests/test_bot.py

from thaichatbot.bot import ThaiChatBot

def test_reply():
    bot = ThaiChatBot("ทดสอบบอท")
    assert bot.reply("สวัสดี").startswith("สวัสดี")
    assert "ทดสอบบอท" in bot.reply("ชื่ออะไร")
    assert "ไม่เข้าใจ" in bot.reply("อากาศเป็นยังไง")  # ไม่รู้เรื่อง
