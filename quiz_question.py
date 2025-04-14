class Question:
    def __init__(self, text, answer, difficulty, category):
        self.text = text
        self.answer = answer.strip().lower()
        self.difficulty = difficulty
        self.category = category

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer

class MCQQuestion(Question):
    def __init__(self, text, options, answer, difficulty, category):
        super().__init__(text, answer, difficulty, category)
        self.options = options

    def check_answer(self, user_answer):
        if user_answer.isdigit():
            try:
                return self.options[int(user_answer) - 1].strip().lower() == self.answer
            except IndexError:
                return False
        return super().check_answer(user_answer)

class TrueFalseQuestion(Question):
    def __init__(self, text, answer, difficulty, category):
        super().__init__(text, answer, difficulty, category)
