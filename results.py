# =============================================
# results.py
# Author(s): Rui Goncalves Pereira
# Created on Sun 22.11.2026
# =============================================

# TODO: currently hardcoded - of which chapter do we want to find out the score? 

#test results
results = [
    {"chapter": "Math", "percentage": 80, "completed_at": "2026-11-15T14:00:00"},
    {"chapter": "Geography", "percentage": 90, "completed_at": "2026-11-18T12:00:00"},
    {"chapter": "Math", "percentage": 60, "completed_at": "2026-11-20T10:00:00"}
]


def get_date(result):
    return result["completed_at"]

def filter_results(results, selected_chapter):
    filtered_results = []

    for result in results:
        if result["chapter"] == selected_chapter:
            filtered_results.append(result)
    
    #sort by the newest results
    filtered_results.sort(key=get_date, reverse=True)

    if not filtered_results:
        print("No results.")
    else:
        for result in filtered_results:
            print(result)

filter_results(results, "Math")