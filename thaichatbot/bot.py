import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ThaiChatBot:
    def __init__(self, name="ไทยแชทบอท", data_path="data/qa_pairs.json"):
        self.name = name
        self.model = SentenceTransformer("distiluse-base-multilingual-cased-v2")

        # ✅ โหลด QA จาก JSON
        with open(data_path, encoding="utf-8") as f:
            raw_data = json.load(f)

        self.qa_pairs = [
            (item["question"], item["answer"].replace("{name}", self.name))
            for item in raw_data
        ]
        self.questions = [q for q, _ in self.qa_pairs]
        self.answers = [a for _, a in self.qa_pairs]
        self.embeddings = self.model.encode(self.questions)

    def reply(self, message: str) -> str:
        user_embedding = self.model.encode([message])
        similarities = cosine_similarity(user_embedding, self.embeddings)[0]
        best_match_idx = np.argmax(similarities)

        if similarities[best_match_idx] > 0.6:
            return self.answers[best_match_idx]
        else:
            return "ขอโทษครับ ฉันยังไม่เข้าใจคำถามนี้ 😅"
