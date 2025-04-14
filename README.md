# 🎮 Quiz Game Engine

A Python-based console quiz game that supports multiple question types, difficulty levels, player profiles, score tracking, and PDF result generation. Built with Object-Oriented Programming (OOP) principles.

---

## 🚀 Features

- Multiple Choice and True/False questions
- Difficulty levels: Easy, Medium, Hard
- Question categories (e.g., Science, History, Tech)
- Score tracking and player profiles
- Shuffled questions every time
- Timer (optional)
- Save/load player stats using CSV
- Export quiz results as PDF

---

## 🧰 Tech Stack

- Python
- OOP (Classes, Inheritance)
- Modules: `csv`, `random`, `datetime`, `fpdf`, `time`

---
## 🛠️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/GowthamKancharla93/quiz-game-engine.git
   cd quiz-game-engine
Install required packages
(Only needed for PDF generation)
pip install fpdf
Run the game
python quiz_game.py
 How to Use
Start the game – Enter your name and choose difficulty and category.

Answer Questions – Questions will appear one by one (MCQ or True/False).

Track Score – Score is calculated and shown at the end.

Save Results – Player stats are stored in a CSV file.

Export to PDF – At the end, your quiz result is saved as a PDF report.

Sample Question Format (CSV)
question,type,options,answer,difficulty,category
"What is the capital of France?",MCQ,"Paris;London;Berlin;Madrid",Paris,Easy,Geography
"Python is a type of snake.",TF,,"True",Easy,Science
Output Files
player_stats.csv – Stores player name and scores.

quiz_result_<playername>.pdf – Auto-generated result sheet.
"Knowledge isn’t power until it is applied."





