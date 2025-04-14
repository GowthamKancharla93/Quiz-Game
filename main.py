import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from quiz_game import QuizGame
from quiz_user_player import Player
from Utils.csv_handler import load_questions, save_player_stats
from Utils.pdf_exporter import export_results_to_pdf


if __name__ == "__main__":
    name = input("Enter your name: ")
    player = Player(name)

    questions = load_questions("data/questions.csv")
    game = QuizGame(player, questions)
    game.start()

    save_player_stats("data/player_stats.csv", player)
    export_results_to_pdf(player)
