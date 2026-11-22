# =============================================
# questions.py
# Author(s): Amanuel Isaak
# Created on Tue 17/11/2026
# =============================================

import csv
from pathlib import Path

Fields = ["topic", "question", "answer"]

def load_flashcard(filename=Path("./data/flashcards.csv")):
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
               print("The file is empty")
               return {}
            if Fields is None:
                print("There're not any fields avaliable")
                return {}
            cards = {}
            for row in reader:
                chapter, question, answer = (
                    (row[i] or "").strip() for i in ("chapter", "question", "answer")
                )
                if chapter and question and answer:
                    cards.setdefault(chapter, []).append({"question": question, "answer": answer})
            return cards
    except (OSError) as e:
        print(f"Could not retrive flashcards {e}")
        return {}

if __name__ == "__main__":
    from pprint import pprint
    cards = load_flashcard()
    pprint(cards)
