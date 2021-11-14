import sys
from PySide2 import QtCore, QtWidgets, QtGui

from ui.NewTask_design import Ui_NewTaskForm


class NewTask(QtWidgets.QWidget):
    send_new_task_data = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(NewTask, self).__init__(parent)
        self.ui = Ui_NewTaskForm()
        self.ui.setupUi(self)

        self.task_name = {'Сделать': 'Do', 'В процессе': 'Doing', 'Выполнено': 'Done'}

        self.ui.comboBoxCategory.addItems(self.task_name.keys())
        self.ui.comboBoxDoer.addItems(['Vasya', 'Petya', 'Vanya'])

        self.ui.pushButton.clicked.connect(self.send_data)

    def send_data(self):
        self.send_new_task_data.emit(
            {'category': self.task_name[self.ui.comboBoxCategory.currentText()],
             'doer': self.ui.comboBoxDoer.currentText(),
             'task_name': self.ui.lineEditTaskName.text(),
             'description': self.ui.plainTextEditDescription.toPlainText(),
             'date_end': self.ui.dateEditEnd.date()})
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = NewTask()
    window.show()
    sys.exit(app.exec_())
