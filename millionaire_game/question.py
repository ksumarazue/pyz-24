from typing import List

class Question:
    def __init__(self, question: str, options: List[str], correct_answer: str, difficulty: str):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def check_answer(self, user_answer: str) -> bool:
        return user_answer == self.correct_answer

    def __str__(self):
        return self._format_question_and_options()

    def _format_question_and_options(self) -> str:
        responses = ""
        for id, res in enumerate(self.options):
            responses += f'{id + 1}) - {res}\n'
        return f"{self.question}\n{responses}"

