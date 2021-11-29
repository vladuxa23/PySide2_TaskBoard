from PySide2 import QtWidgets


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.initUi()

    def initUi(self):
        """Функция донастройки Ui"""

        # Ввод имени пользователя
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setPlaceholderText("Введите ваше логин")

        # Ввод пароля
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setPlaceholderText("Введите ваш пароль")

        # Кнопка login
        self.buttonLogin = QtWidgets.QPushButton('Login')
        self.buttonLogin.clicked.connect(self.handleLogin)

        # Настройка слоя виджетов
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)

    login = Login()
    login.show()

    sys.exit(app.exec_())
