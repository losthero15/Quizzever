from data import load_questions
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = load_questions()
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
