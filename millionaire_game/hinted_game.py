from game import Game

class HintGame(Game):
    hints_allowed = 3
    def __init__(self, questions):
        super().__init__(questions)

    def request_hint(self, current_question):
        if self.hints_allowed > 0:
            print(f"Hint: The answer starts with {current_question.correct_answer[0]}")
            self.hints_allowed -= 1
        else:
            print("No hints left!")

    @classmethod
    def set_hints_allowed(cls, number):
        cls.hints_allowed = number



def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4",  difficulty='easy'),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", difficulty='easy'),
    ]

    game1 = HintGame(question_list)
    game2 = HintGame(question_list)

    print(game1.hints_allowed)
    print(game2.hints_allowed)
    HintGame.set_hints_allowed(5)

    print(game1.hints_allowed)
    print(game2.hints_allowed)



if __name__ == '__main__':
    main()