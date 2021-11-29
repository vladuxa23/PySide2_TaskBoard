import sys
from PySide2 import QtCore, QtWidgets, QtGui

from ui.window_design_new_task import Ui_NewTaskForm


class NewTask(QtWidgets.QWidget):
    send_new_task_data = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(NewTask, self).__init__(parent)
        self.ui = Ui_NewTaskForm()
        self.ui.setupUi(self)

        self.task_name = {'Сделать': 'WidgetDo',
                          'В процессе': 'WidgetDoing',
                          'Выполнено': 'WidgetDone'}

        self.ui.comboBoxCategory.addItems(self.task_name.keys())
        self.ui.comboBoxDoer.addItems(['Vasya', 'Petya', 'Vanya'])

        self.ui.pushButton.clicked.connect(self.send_data)

    def send_data(self):
        data = {'category': self.task_name[self.ui.comboBoxCategory.currentText()],
                'doer': self.ui.comboBoxDoer.currentText(),
                'task_name': self.ui.lineEditTaskName.text(),
                'description': self.ui.plainTextEditDescription.toPlainText(),
                'date_end': self.ui.dateEditEnd.date().toString()}
        self.send_new_task_data.emit(data)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = NewTask()
    window.show()
    sys.exit(app.exec_())
