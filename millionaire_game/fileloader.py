import json
from question import Question


def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    questions = []
    for item in data:
        question = Question(
            item['question'],
            item['options'],
            item['correct_answer'],
            item['difficulty']
        )
        questions.append(question)
    return questions

def save_to_file(score, current_question, filename):
    game_score = {'score': score, 'current_index' : current_question}
    with open(filename, 'w') as file:
        json.dump(game_score, file, indent=4)


