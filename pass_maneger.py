import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_recent_passwords()

    def initUI(self):
        self.setWindowTitle('Password Manager')
        self.setGeometry(100, 100, 400, 300)

        self.service_label = QLabel('Сервис:')
        self.service_input = QLineEdit()
        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.add_button = QPushButton('Добавить')
        self.recent_passwords_label = QLabel('Недавно добавленные пароли:')
        self.recent_passwords_textedit = QTextEdit()
        self.recent_passwords_textedit.setReadOnly(True)

        layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.service_label)
        input_layout.addWidget(self.service_input)
        input_layout.addWidget(self.password_label)
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)
        layout.addWidget(self.recent_passwords_label)
        layout.addWidget(self.recent_passwords_textedit)
        self.setLayout(layout)
        self.add_button.clicked.connect(self.add_password)

    def add_password(self):
        service = self.service_input.text()
        password = self.password_input.text()
        if service and password:
            with open('passwords.txt', 'a') as file:
                file.write(f'{service} - {password}\n')
            self.service_input.clear()
            self.password_input.clear()
            self.load_recent_passwords()

    def load_recent_passwords(self):
        with open('passwords.txt', 'r') as file:
            lines = file.readlines()
            recent_passwords = lines[-5:]
            self.recent_passwords_textedit.clear()
            for password in recent_passwords:
                self.recent_passwords_textedit.append(password.strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec_())
