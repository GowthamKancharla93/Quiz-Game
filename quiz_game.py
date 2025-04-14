import random
import time

class QuizGame:
    def __init__(self, player, questions):
        self.player = player
        self.questions = questions
        random.shuffle(self.questions)

    def start(self):
        print(f"\nWelcome {self.player.name} to the Quiz Game!\n")

        for question in self.questions:
            print(f"\nCategory: {question.category} | Difficulty: {question.difficulty}")
            print(question.text)

            if hasattr(question, 'options'):
                for i, option in enumerate(question.options):
                    print(f"{i + 1}. {option}")

            start_time = time.time()
            answer = input("Your answer: ")
            elapsed = round(time.time() - start_time)

            if elapsed > 20:
                print(" Time's up!")
                continue

            if question.check_answer(answer):
                print(" Correct!")
                self.player.score += 1
                self.player.update_stats(question.category, True)
            else:
                print(f" Wrong! Correct answer: {question.answer}")
                self.player.update_stats(question.category, False)

        print(f"\n Game Over! Final Score: {self.player.score}")
