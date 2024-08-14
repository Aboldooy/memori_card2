from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from main_window import *
from menu_window import *

from questions_controller import *

q1 = Question(    
    question="Скільки бегимотів в людині",
    answer="2",
    wrong_answer1="52",
    wrong_answer2="300",
    wrong_answer3="завтра"
)

q2 = Question(
    question="да",
    answer="прижок с передподвипердом",
    wrong_answer1="нет",
    wrong_answer2="возможно",
    wrong_answer3="не"
)

question_controller = QuestionController()
question_controller.add_answer(q1)
question_controller.add_answer(q2)

def show_questions():
    result_gbox.hide()
    answers_gbox.show()
    question_controller.show_question()
    
def show_results():
    result_gbox.show()
    answers_gbox.hide()
    
def check_answer():
    if give_answer_pbtn.text() == "Відповісти":
        show_results()
        give_answer_pbtn.setText("Наступне питання")
        
    elif give_answer_pbtn.text() == "Наступне питання":
        show_questions()
        give_answer_pbtn.setText("Відповісти")
    
def show_menu():
    window_menu.show()
    window_main.hide()
    
def show_main():
    window_main.show()
    window_menu.hide()
    
def connect_buttons():
    menu_pbtn.clicked.connect(show_menu)
    give_answer_pbtn.clicked.connect(check_answer)
    back_to_main_pbtn.clicked.connect(show_main)
    