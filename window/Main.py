import sys
from PyQt6.QtWidgets import *
import random
from PyQt6.QtCore import QTimer
import string

class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("окно")

        label_login = QLabel("Login:")
        login_edit = QLineEdit()
        label_password = QLabel("Password:")
        password_edit = QLineEdit()
        button_auth = QPushButton("Enter")
        button_exit = QPushButton("Exit")
        
        layout = QVBoxLayout()
        layout.addWidget(label_login)
        layout.addWidget(login_edit)
        layout.addWidget(label_password)
        layout.addWidget(password_edit)
        layout.addWidget(button_auth)
        layout.addWidget(button_exit)

        button_auth.clicked.connect(self.auth)
        button_exit.clicked.connect(self.exit)

        self.setLayout(layout)
        
    def auth(self):        
        self.test = Captcha()
        self.test.show()
        
    def exit(self):
        quit()

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_edit = QLineEdit()
        self.captcha_btn = QPushButton("Проверить")
        self.timer_label = QLabel("Таймер: 10")
        self.count = 10
        self.timer_label.setText(str(self.count))
        self.timer = QTimer()
        
        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_btn)
        layout.addWidget(self.captcha_edit)
        layout.addWidget(self.timer_label)

        self.captcha_btn.clicked.connect(self.captcha_click)
        self.timer.timeout.connect(self.timer_tick)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def captcha_click(self):
        if self.captcha_edit.text() == self.captcha.text():
            QMessageBox.information(self, "Верно", "Верно")
            Captcha.close(self)
        else:
            self.captcha_edit.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Ошибка")  

    def timer_tick(self):
        self.timer.start(1000)
        self.timer_counter = 10
        self.count -= 1
        self.timer_label.setText(str(self.count))

        if self.count == 0:
            self.timer.stop()
            self.captcha_edit.setDisabled(False)      

app= QApplication(sys.argv)
exe = Main()
exe.show()
app.exec()