# =============================================
# questions.py
# Author(s): Amanuel Isaak
# Created on Tue 22/11/2026
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


# Add flashcard
import csv

def add_flashcard():
    print("\nAdd a new flashcard")
    
    chapter=input("Enter chapter: ").strip()

    while chapter=="":
        print("Chapter cannot be empty.")
        chapter=input("Enter chapter:").strip() 

    question=input("Enter chapter: ").strip()

    while question == "":
        print("Question cannot be empty.")
        question = input("Enter question: ").strip()

    answer = input("Enter correct answer: ").strip()

    while answer == "":
        print("Answer cannot be empty.")
        answer = input("Enter correct answer: ").strip()


    # To save flashcard in the file
    with open("data/flashcards.csv", "a", newline="") as file:

         writer = csv.DictWriter(
            file,
            fieldnames=["chapter", "question", "answer"])

         writer.writerow({
            "chapter": chapter,
            "question": question,
            "answer": answer})

    print("Flashcard successfully saved!")