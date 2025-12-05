import json
import random
from pathlib import Path

class QuestionManager:
    def __init__(self, file_path: str = "data/questions.json"):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"Fichier questions introuvable : {self.file_path}")

        with self.file_path.open("r", encoding="utf-8") as f:
            self.questions = json.load(f)

        self.used = set()

    def get_random_question(self):
        available = [q for q in self.questions if q["question"] not in self.used]

        if not available:
            self.used.clear()
            available = self.questions

        q = random.choice(available)
        self.used.add(q["question"])
        return q
