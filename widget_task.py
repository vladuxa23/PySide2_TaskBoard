import sys
from PySide2 import QtCore, QtWidgets, QtGui


class TaskWidget(QtWidgets.QFrame):

    def __init__(self, category, doer, task_name, description, date_end, parent=None,):
        super(TaskWidget, self).__init__(parent)

        self.setObjectName("TaskFrame")

        self.category = category
        self.doer = doer
        self.task_name = task_name
        self.description = description
        self.date_end = date_end

        self.initUi()

    def initUi(self):

        self.setStyleSheet("""
        #TaskFrame {
            border: 1px solid black;
            border-radius: 5px;
            background-color: #fff;
        }
        QLabel {
        
        }
        """)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtGui.Qt.AlignTop)
        self.setLayout(layout)
        self.frame = QtWidgets.QFrame()

        self.setMinimumSize(150, 200)
        self.setMaximumHeight(200)

        self.labelName = QtWidgets.QLabel(f"Название: {self.task_name}")
        self.labelDoer = QtWidgets.QLabel(f"Исполнитель: {self.doer}")
        self.labelDescription = QtWidgets.QLabel(f"Описание:")
        self.textEditDescription = QtWidgets.QPlainTextEdit(self.description)
        self.textEditDescription.setReadOnly(True)
        self.labelDateEnd = QtWidgets.QLabel(f"Выполнить до:\n{self.date_end}")

        layout.addWidget(self.labelName)
        layout.addWidget(self.labelDoer)
        layout.addWidget(self.labelDescription)
        layout.addWidget(self.textEditDescription)
        layout.addWidget(self.labelDateEnd)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = TaskWidget(**{'category': 'WidgetDo', 'doer': 'Vasya', 'task_name': '12354', 'description': '1213131231 qs asd asddwqad awdawd awd awd3123', 'date_end': QtCore.QDate(2000, 1, 1)})
    window.show()
    sys.exit(app.exec_())
