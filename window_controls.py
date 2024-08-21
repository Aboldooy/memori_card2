from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from main_window import *
from menu_window import *

from start_question import question_controller
from questions_controller import Question

def show_questions():
    result_gbox.hide()
    answers_gbox.show()
    question_controller.show_question()
    
def show_results():
    result_gbox.show()
    answers_gbox.hide()
    
def check_answer():
    if give_answer_pbtn.text() == "Відповісти":

        if question_controller.check_is_right_answer():
            result_lbl.setText("Правильна відповідь")
        else:
            result_lbl.setText("Неправильна відповідь")

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

def add_question():
    new_question = Question(
        question=question_ledit.text(),
        answer=answer_ledit.text(),
        wrong_answer1=wrong1_ledit.text(),
        wrong_answer2=wrong2_ledit.text(),
        wrong_answer3=wrong3_ledit.text()
    )
    question_controller.add_answer(new_question)
    
    question_ledit.clear()
    answer_ledit.clear()
    wrong1_ledit.clear()
    wrong2_ledit.clear()
    wrong3_ledit.clear()

def remove_question():
    question_text = questions_list.selectedItems()
    if question_text:
        question_text = question_text[0].text()

        question_controller.remove_answer(question_text)
    
def connect_buttons():
    menu_pbtn.clicked.connect(show_menu)
    give_answer_pbtn.clicked.connect(check_answer)
    back_to_main_pbtn.clicked.connect(show_main)

    add_question_pbtn.clicked.connect(add_question)
    remove_question_pbtn.clicked.connect(remove_question)
    