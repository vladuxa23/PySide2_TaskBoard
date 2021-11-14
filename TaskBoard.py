import sys
from PySide2 import QtCore, QtWidgets, QtGui

from ui.TaskBoard_design import Ui_TaskBoard
from ui.TaskWidget import TaskWidget
from NewTask import NewTask


class TaskBoard(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(TaskBoard, self).__init__(parent)
        self.ui = Ui_TaskBoard()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):

        self.ui.pushButton.clicked.connect(self.show_new_task_widget)
        self.ui.actionExit.triggered.connect(lambda: self.close())

        self.widgetDo = QtWidgets.QWidget()
        self.widgetDo.setObjectName("WidgetDo")
        self.widgetDo.setLayout(QtWidgets.QVBoxLayout())

        self.widgetDoing = QtWidgets.QWidget()
        self.widgetDoing.setObjectName("WidgetDoing")
        self.widgetDoing.setLayout(QtWidgets.QVBoxLayout())

        self.widgetDone = QtWidgets.QWidget()
        self.widgetDone.setObjectName("WidgetDone")
        self.widgetDone.setLayout(QtWidgets.QVBoxLayout())

        self.ui.scrollAreaDo.setWidget(self.widgetDo)
        self.ui.scrollAreaDoing.setWidget(self.widgetDoing)
        self.ui.scrollAreaDone.setWidget(self.widgetDone)

    def show_new_task_widget(self):
        self.new_task_widget = NewTask()

        self.new_task_widget.send_new_task_data.connect(self.add_new_task,
                                                        QtCore.Qt.QueuedConnection)

        self.new_task_widget.show()

    def add_new_task(self, data):
        print(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = TaskBoard()
    window.show()
    sys.exit(app.exec_())
