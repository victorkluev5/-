import sys
from PyQt6.QtWidgets import *

class test_car(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест по выбору автомобиля")
        self.setFixedSize(400, 300)

        self.current_question = 0
        self.total_questions = 3
        self.answers = []

        self.question_label = QLabel()
        self.answer_radio_buttons = []
        self.next_button = QPushButton("Далее")
        self.next_button.setDisabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.question_label)

        for i in range(4):
            radio_button = QRadioButton()
            radio_button.clicked.connect(self.enable_next_button)
            self.answer_radio_buttons.append(radio_button)
            layout.addWidget(radio_button)

        layout.addWidget(self.next_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.questions = [
            {
                "question": "Какой тип автомобиля вы предпочитаете?",
                "answers": ["Седан", "Хэтчбек", "Внедорожник", "Купе"]
            },
            {
                "question": "Какой бюджет у вас на автомобиль?",
                "answers": ["До 20 000$", "20 000$ - 40 000$", "40 000$ - 60 000$", "Более 60 000$"]
            },
            {
                "question": "Какие опции вам необходимы?",
                "answers": ["Кондиционер", "Навигационная система", "Камера заднего вида", "Круиз-контроль"]
            }
        ]

        self.load_question(self.current_question)

        self.next_button.clicked.connect(self.next_question)

    def load_question(self, question_index):
        self.question_label.setText(self.questions[question_index]["question"])
        answers = self.questions[question_index]["answers"]

        for i in range(4):
            if i < len(answers):
                self.answer_radio_buttons[i].setText(answers[i])
                self.answer_radio_buttons[i].setChecked(False)
                self.answer_radio_buttons[i].setHidden(False)
            else:
                self.answer_radio_buttons[i].setHidden(True)

    def enable_next_button(self):
        self.next_button.setDisabled(False)

    def next_question(self):
        self.answers.append(self.get_selected_answer())
        self.current_question += 1

        if self.current_question < self.total_questions:
            self.load_question(self.current_question)
            self.next_button.setDisabled(True)
        else:
            self.show_result()

    def get_selected_answer(self):
        for i in range(4):
            if self.answer_radio_buttons[i].isChecked():
                return self.answer_radio_buttons[i].text()

    def show_result(self):
        result = "Результаты:\n"
        for i in range(self.total_questions):
            result += f"Вопрос {i+1}: {self.questions[i]['question']}\n"
            result += f"Ответ: {self.answers[i]}\n\n"
        QMessageBox.information(self, "Результаты", result)
       
        with open('resultate.txt', 'w') as f: 
            resultat = [result] 
            f.writelines(resultat) 
