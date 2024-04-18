# TODO
from game import Game


class TimedGame(Game):
    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.time_limit = time_limit
        self.remaining_time = time_limit

    def submit_answer(self, answer):
        if self.remaining_time <= 0:
            print("Time's up!")
            return False

        current_question = self.questions[self._current_question_index - 1]
        if current_question.check_answer(answer):
            self._score += 100
            print(f"Remaining time: {self.remaining_time}")
            return True
        else:
            self.remaining_time -= 10  # Przykładowa kara czasowa
            print(f"Remaining time: {self.remaining_time}")
            return False