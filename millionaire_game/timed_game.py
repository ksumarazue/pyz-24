from game import Game

class TimedGame(Game):# Inheritance(dziedziczenie) from the class Game
    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.time_limit = time_limit

    def submit_answer(self, answer):
        if super().submit_answer(answer):
            print(f"Correct! Remaining time: {self.time_limit}")
            return True
        elif not super().submit_answer(answer):
            self.time_limit -= 10
            if self.time_limit == 0:
                print(f"Wrong! No more time left!")
                return False
            else:
                print(f"Wrong! Time penalty applied. Remaining time: {self.time_limit}")
                return True