from game import Game

class TimedGame(Game):
    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.time_limit = time_limit

    def submit_answer(self, answer):
        if super().submit_answer(answer):
            print(f"Correct! Remaining time: {self.time_limit}")
            return True
        elif self.time_limit > 0:
            self.time_limit -= 10
            print(f"Wrong! Time penalty applied. Remaining time: {self.time_limit}")
            return True
        else:
            print(f"Wrong! No more time left!")
            return False