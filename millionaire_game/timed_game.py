from typing import Optional
from typing import
from game import Game
import threading
import time



class TimedGame(Game):
    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.timer = None
        self.time_limit = time_limit

    def start_timer(self):
        self.timer = threading.Timer(self.time_per_question, self.time_up)
        self.timer.start()


    def timed_up(self):
        print('Time over. Method timed up')
        self.submit_answer(None)


    def get_next_question(self) -> Optional[Question]:
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            self.start_timer()
            return question
        else:
            return None

    def submit_answer(self, answer):
        if self.timer:
            self.timer.cancel()

        if answer is None:
            print('Didnt answer on time!')
            return False

        if super().submit_answer(answer):
            print(f"Correct! Remaining time: {self.time_limit}")
            return True
        else
        # elif not super().submit_answer(answer):
        #     self.time_limit -= 10
        #     if self.time_limit == 0:
        #         print(f"Wrong! No more time left!")
        #         return False
        #     else:
        #         print(f"Wrong! Time penalty applied. Remaining time: {self.time_limit}")
        #         return True

    # def _time_game(time_lim):
    #     for i in time_lim:
    #         time.sleep(1)
    #     print('\nTimes up thread!')
    #
    # def time_limit_game(self, time_lim):
    #     self.timelim = time_lim
    #     thread = threading.Thread(target=self._time_game, args=(self.timelim,))
    #     thread.start()
    #
    #     # thread.join()
    #     if not thread.is_alive():
    #         # thread.join()
    #         return False




    def __str__(self):
        return f'Time--> {self.time_limit}'



def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4",  difficulty='easy'),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", difficulty='easy'),
    ]

    game = TimedGame(question_list, 10)
    print(game)


if __name__ == '__main__':
    main()