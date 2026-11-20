# =============================================
# questions.py
# Author(s): Rui Goncalves Pereira
# Created on Tue 17/11/2026
# =============================================

def check_answer(answer, question_answer):
    while answer.strip() == "":
        print("Please enter an answer")
        answer = input("Answer:")

    if answer.strip().lower() != question_answer.strip().lower():
        return 0
    return 1
        
    


check_answer("True", "True")