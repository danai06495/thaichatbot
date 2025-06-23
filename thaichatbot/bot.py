# thaichatbot/bot.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ThaiChatBot:
    def __init__(self, name="ไทยแชทบอท"):
        self.name = name
        self.model = SentenceTransformer('distiluse-base-multilingual-cased-v2')  # รองรับภาษาไทยดี
        self.qa_pairs = [
            ("สวัสดี", "สวัสดีครับ 😊"),
            ("ชื่ออะไร", f"ฉันชื่อ {self.name}"),
            ("คุณทำอะไรได้บ้าง", "ฉันสามารถตอบคำถามทั่วไปเป็นภาษาไทยได้"),
            ("ลาก่อน", "เจอกันใหม่นะครับ 👋"),
        ]
        self.questions = [q for q, a in self.qa_pairs]
        self.answers = [a for q, a in self.qa_pairs]
        self.embeddings = self.model.encode(self.questions)

    def reply(self, message: str) -> str:
        user_embedding = self.model.encode([message])
        similarities = cosine_similarity(user_embedding, self.embeddings)[0]
        best_match_idx = np.argmax(similarities)

        if similarities[best_match_idx] > 0.6:
            return self.answers[best_match_idx]
        else:
            return "ขอโทษครับ ฉันยังไม่เข้าใจคำถามนี้ 😅"
