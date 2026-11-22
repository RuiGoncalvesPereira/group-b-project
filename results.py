# =============================================
# results.py
# Author(s): Rui Goncalves Pereira
# Created on Sun 22.11.2026
# =============================================

# TODO: currently hardcoded - of which chapter do we want to find out the score? 
selected_chapter = "Math"
#test results
results = [
    {"chapter": "Math", "percentage": 80},
    {"chapter": "Geography", "percentage": 90},
    {"chapter": "Math", "percentage": 60}
]


#find out the scores of the chapter we selected
for result in results:
    if result["chapter"] == selected_chapter:
        print("Found!")
