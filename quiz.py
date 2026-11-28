# =============================================
# quiz.py
# Author(s): Rui Goncalves Pereira
# Created on Tue 17/11/2026
# =============================================

def check_answer(answer, question_answer):
    while answer.strip() == "":
        print("Please enter an answer")
        answer = input("Answer:")

    if answer.strip().lower() != question_answer.strip().lower():
        print(f"Incorrect!\nCorrect answer: {question_answer}")
        return 0
    print("Correct!")
    return 1
        
    

result = check_answer("", "True")
print(result)

# reviw mistakes 
def review_mistakes(mistakes):

    print("\n--- REVIEW YOUR MISTAKES ---")

mistakes = []
mistakes.append({
     "question": question,
    "user_answer": user_answer,
    "correct_answer": answer
})

if len(mistakes) == 0:
    print("No mistakes to review.")

else:
     for item in mistakes:
            print("\nQuestion:")
            print(item["question"])
            print(f"Your answer: {item['user_answer']}")
            print(f"Correct answer: {item['correct_answer']}")
