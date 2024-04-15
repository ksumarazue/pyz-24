class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

    def __str__(self):
        return self._format_question_and_options()

    def _format_question_and_options(self):
        responses = ""
        for id, res in enumerate(self.options):
            responses += f'{id + 1}) - {res}\n'
        return f"{self.question}\n{responses}"
    # def __str__(self):
    #     return self._format_question_and_options()
    #     # return f"{self.question}\nOptions: {self.options}"
    #
    # def _format_question_and_options(self):
    #     responses = ""
    #     for id, res in enumerate(self.options):
    #         responses += f'{id + 1}) - {res}\n'
    #     return f"{self.questions}\n{responses}"