import requests
import json
import html

class OpenTriviaWrapper:
    CATEGORY_SCIENCE = 17
    CATEGORY_COMPUTERS = 18
    CATEGORY_BOOKS = 10
    CATEGORY_FILM = 11
    CATEGORY_MUSIC = 12
    
    DIFFICULTY_EASY = "easy"
    DIFFICULTY_MEDIUM = "medium"
    DIFFICULTY_HARD = "hard"
    
    QUESTION_TYPE_BOOLEAN = "boolean"
    
    
    def __init__(self):
        self.base_url = "https://opentdb.com/api.php"

    def get_questions(self, amount=10, category="CATEGORY_BOOKS", difficulty=DIFFICULTY_EASY, type=QUESTION_TYPE_BOOLEAN):
        params = {
            "amount": amount,
            "category": category,
            "difficulty": difficulty,
            "type": type
        }
        print(params)
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            results = response.json()["results"]
            for result in results:
                result["question"] = html.unescape(result["question"])
                result["category"] = html.unescape(result["category"])
                result["correct_answer"] = html.unescape(result["correct_answer"])
            return results
        else:
            return None
        
def write_to_json(questions, filename):
    data = []
    for question in questions:
        data.append({
            "question": question["question"],
            "answer": question["correct_answer"]
        })
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
