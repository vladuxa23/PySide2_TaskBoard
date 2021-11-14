import sys
from PySide2 import QtCore, QtWidgets

from ui.TaskBoard_design import Ui_TaskBoard
from TaskWidget import TaskWidget
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

        self.widgetDo = QtWidgets.QGroupBox("Сделать")
        self.widgetDo.setObjectName("WidgetDo")
        self.widgetDo.setLayout(QtWidgets.QVBoxLayout())

        self.widgetDoing = QtWidgets.QGroupBox("В процессе")
        self.widgetDoing.setObjectName("WidgetDoing")
        self.widgetDoing.setLayout(QtWidgets.QVBoxLayout())

        self.widgetDone = QtWidgets.QGroupBox("Выполнено")
        self.widgetDone.setObjectName("WidgetDone")
        self.widgetDone.setLayout(QtWidgets.QVBoxLayout())

        self.ui.scrollAreaDo.setWidget(self.widgetDo)
        self.ui.scrollAreaDoing.setWidget(self.widgetDoing)
        self.ui.scrollAreaDone.setWidget(self.widgetDone)

        self.stretchy_spacer_thing = QtWidgets.QSpacerItem(10, 10,
                                                           QtWidgets.QSizePolicy.Minimum,
                                                           QtWidgets.QSizePolicy.Expanding)

    def show_new_task_widget(self):
        self.new_task_widget = NewTask()

        self.new_task_widget.send_new_task_data.connect(self.add_new_task,
                                                        QtCore.Qt.QueuedConnection)

        self.new_task_widget.show()

    def add_new_task(self, data):

        widget = self.getWidgetByObjectName(data["category"])

        try:
            widget.layout().removeItem(self.stretchy_spacer_thing)
        except Exception as err:
            print(err)

        widget.layout().addWidget(TaskWidget(**data))
        widget.layout().addItem(self.stretchy_spacer_thing)

    @staticmethod
    def getWidgetByObjectName(widget_name):
        widgets = QtWidgets.QApplication.instance().topLevelWidgets()
        widgets = widgets + QtWidgets.QApplication.instance().allWidgets()
        for x in widgets:
            print(x.objectName())
            if str(x.objectName()) == widget_name:
                return x


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = TaskBoard()
    window.show()
    sys.exit(app.exec_())
