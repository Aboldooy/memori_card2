'''
Файл, в якому відтворено інтерфейс меню
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

window_menu = QWidget() # вікно меню
window_menu_layout = QVBoxLayout() # лейаут для вікна меню

# ВІДЖЕТИ ВІКНА # 

questions_list = QListWidget()

add_question_pbtn = QPushButton("Додати питання")
remove_question_pbtn = QPushButton("Видалити питання")

question_ledit = QLineEdit()
answer_ledit = QLineEdit()
wrong1_ledit = QLineEdit()
wrong2_ledit = QLineEdit()
wrong3_ledit = QLineEdit()

back_to_main_pbtn = QPushButton("Повернутись в меню")

# ЛЕЙАУТИ ВІКНА # 

buttons_row_layout = QHBoxLayout()
question_form_layout = QFormLayout()

# РОЗТАШОВУЄМО ВІДЖЕТИ У ЛЕЙАУТАХ #

window_menu_layout.addWidget(questions_list)

buttons_row_layout.addWidget(add_question_pbtn)
buttons_row_layout.addWidget(remove_question_pbtn)
window_menu_layout.addLayout(buttons_row_layout)

question_form_layout.addRow("Введіть питання: ", question_ledit)
question_form_layout.addRow("Введіть відповідь: ", answer_ledit)
question_form_layout.addRow("Введіть неправильне: ", wrong1_ledit)
question_form_layout.addRow("Введіть неправильне: ", wrong2_ledit)
question_form_layout.addRow("Введіть неправильне: ", wrong3_ledit)
window_menu_layout.addLayout(question_form_layout)

window_menu_layout.addWidget(back_to_main_pbtn)

window_menu.setLayout(window_menu_layout)