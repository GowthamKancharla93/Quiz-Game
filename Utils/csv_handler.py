import csv
from quiz_question import MCQQuestion, TrueFalseQuestion

def load_questions(filename):
    questions = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qtype = row['type']
            if qtype == "MCQ":
                options = row['options'].split('|')
                questions.append(MCQQuestion(
                    row['text'], options, row['answer'],
                    row['difficulty'], row['category']))
            elif qtype == "TF":
                questions.append(TrueFalseQuestion(
                    row['text'], row['answer'],
                    row['difficulty'], row['category']))
    return questions

def save_player_stats(filename, player):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([player.name, player.score])
