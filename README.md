# ThaiChatBot 🇹🇭🤖

โปรเจกต์ Python AI ChatBot ภาษาไทยอย่างง่าย  
ใช้เทคนิค sentence-transformers + cosine similarity เพื่อทำ chatbot ที่ตอบคำถามตามข้อมูลที่กำหนด

---

## คุณสมบัติ

- รองรับการถามตอบภาษาไทยด้วย AI เบื้องต้น
- ใช้งานง่าย ติดตั้งและเรียกใช้ผ่าน Python
- ขยายคำถาม-คำตอบได้ด้วยการเพิ่มข้อมูลในไฟล์
- เหมาะสำหรับผู้เริ่มต้นทำ chatbot ภาษาไทย

---

## วิธีติดตั้ง

```bash
git clone https://github.com/danai06495/thaichatbot.git
cd thaichatbot
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
pip install -e .
