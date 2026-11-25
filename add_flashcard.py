#======================================
#add_flashcard.py
#Author: Marisa
#created on 25/11/2026
#======================================

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