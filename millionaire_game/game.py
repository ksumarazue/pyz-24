class Game:
    def __init__(self, questions):
        self.questions = questions
        self._current_question_index = 0
        self._score = 0
    
    def get_next_question(self):
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            return question
        else:
            return None
        
    def submit_answer(self, answer):
        current_question = self.questions[self._current_question_index - 1]
        if current_question.check_answer(answer):
            self._score += 100
            return True
        else:
            return False

    def get_score(self):
        return f'{self._score} PLN'

    def __str__(self):
        return f"Current score: {self._score}"

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, index):
        if index <= len(self.questions):
            return self.questions[index]
        else:
            return None

    def __setitem__(self, index, value):
        self.questions[index] = value

from question import Question
question_list = [
    Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
    Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
    Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
    ]

obj = Game(question_list)
print(obj.__len__())

print()
print(obj[4])




# Utwórz dla TimedGame i HintGame specyficzne dla nich metody specjalne __str__

# Dodatkowo do klasy Game dodaj __getitem__ i __setitem__
# jako metody, które można użyć do bezpośredniego dostępu do pytań w grze,
# traktując obiekt gry jak kontener.
# len - metoda może zwracać liczbę pytań w grze.


    # Przykład użycia
    # game[0] zwróci pierwsze pytanie
    # game[0] = new_question ustawi nowe pytanie na pierwszej pozycji, gdzie new_question jest obiektem typu Question