from question import Question
from typing import List, Optional
from fileloader import load_questions_from_file
def log_answers(func):
    def wrapper(self, *args):
        print('*' * 30)
        result = func(self, *args)
        print('Your answer:', args[0])
        print('Score: ', self._score)
        return result
    return wrapper

def check_answer_correct(question: Question, answer: str):
    """check if answer is correct"""
    return question.correct_answer == answer


class Game:
    def __init__(self, questions: List[Question]):
        self.questions = questions
        self._current_question_index = 0
        self._score = 0
        self.check = check_answer_correct

    @classmethod
    def from_json(cls, filename):
        questions = load_questions_from_file(filename)
        return cls(questions)

    def __str__(self):
        return f"Current score: {self._score}"

    def __len__(self) -> int:
        return len(self.questions)

    def __getitem__(self, index) -> Optional[Question]:
        """ get question for the Game until available  """
        if index < len(self.questions):
            return self.questions[index]
        else:
            return None

    def __setitem__(self, index: int, value: Question) -> None:
        if index < len(self.questions):
            self.questions[index] = value
        else:
            raise IndexError

    def get_next_question(self) -> Optional[Question]:
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            return question
        else:
            return None

    @log_answers
    def submit_answer(self, answer: str) -> bool:
        current_question = self.questions[self._current_question_index - 1]
        if self.check(current_question, answer):
            self._score += 100
            return True
        else:
            return False

    def get_score(self) -> str:
        return f'{self._score} PLN'

    @staticmethod
    def is_valid(answer_nr: int, options: list) -> bool:
        return 0 < answer_nr <= len(options)


def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
    ]

    game = Game(question_list)
    print(len(game))
    print(game[0])
    game[0] = Question("What is 5 + 2?", ["3", "7", "2", "5"], "7")
    print(game[0])

if __name__ == '__main__':
    main()