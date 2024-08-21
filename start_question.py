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