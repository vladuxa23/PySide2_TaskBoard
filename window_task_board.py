import sys
from PySide2 import QtCore, QtWidgets

from ui.window_design_task_board import Ui_TaskBoard
from widget_task import TaskWidget
from window_new_task import NewTask

from models import Tasks, Session


class TaskBoard(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(TaskBoard, self).__init__(parent)
        self.ui = Ui_TaskBoard()
        self.ui.setupUi(self)

        self.session = Session()

        self.initUi()

    def initUi(self):
        """Функция донастройки Ui"""

        self.ui.pushButton.clicked.connect(self.show_new_task_widget)
        self.ui.actionExit.triggered.connect(lambda: self.close())

        # Настраиваем окно widgetDo
        self.widgetDo = QtWidgets.QGroupBox("Сделать")
        self.widgetDo.setObjectName("WidgetDo")
        self.widgetDo.setLayout(QtWidgets.QVBoxLayout())

        # Настраиваем окно widgetDoing
        self.widgetDoing = QtWidgets.QGroupBox("В процессе")
        self.widgetDoing.setObjectName("WidgetDoing")
        self.widgetDoing.setLayout(QtWidgets.QVBoxLayout())

        # Настраиваем окно widgetDone
        self.widgetDone = QtWidgets.QGroupBox("Выполнено")
        self.widgetDone.setObjectName("WidgetDone")
        self.widgetDone.setLayout(QtWidgets.QVBoxLayout())

        # Настраиваем возможность скрола в виджетах
        self.ui.scrollAreaDo.setWidget(self.widgetDo)
        self.ui.scrollAreaDoing.setWidget(self.widgetDoing)
        self.ui.scrollAreaDone.setWidget(self.widgetDone)

        # Добавляем стретч, чтобы виджет прилипал к верху
        self.stretchy_spacer_thing = QtWidgets.QSpacerItem(10, 10,
                                                           QtWidgets.QSizePolicy.Minimum,
                                                           QtWidgets.QSizePolicy.Expanding)

        # Добавляем таски при загрузке
        for elem in self.get_tasks_from_db():
            self.add_task_to_board(elem)

    def get_tasks_from_db(self):
        """Функция загружает при открытии все таски из БД"""

        # TODO: Подумать, возможно есть смысл убрать получение тасок в models
        # Получаем из БД все таски
        tasks = self.session.query(Tasks).all()
        return [{k: v for k, v in x.__dict__.items() if
                 k != "_sa_instance_state" and k != 'id'} for x in tasks]

    def show_new_task_widget(self):
        """Функция открывает дочернее окно добавления новой таски"""
        self.new_task_widget = NewTask()
        self.new_task_widget.send_new_task_data.connect(
            self.add_new_task_to_board,
            QtCore.Qt.QueuedConnection)
        self.new_task_widget.show()

    def add_task_to_board(self, data):
        """Функция добавляет таску на конкретный виджет на борде"""
        # Получаем из данных, в какой виджет надо добавить таску
        widget = self.getWidgetByObjectName(data["category"])

        # Удаляем стретч
        try:
            widget.layout().removeItem(self.stretchy_spacer_thing)
        except Exception as err:
            print(err)

        # Добавляем таску на борд
        widget.layout().addWidget(TaskWidget(**data))
        # Добавляем стретч
        widget.layout().addItem(self.stretchy_spacer_thing)

    def add_new_task_to_board(self, data):
        """Функция добавляет новую таску в БД"""
        # Добавляем таску на борд
        self.add_task_to_board(data)
        # Добавляем таску в БД
        self.session.add(Tasks(**data))
        self.session.commit()

    @staticmethod
    def getWidgetByObjectName(widget_name):
        """Функция возвращает ссылку на виджет,
        в который надо поместить таску"""

        widgets = QtWidgets.QApplication.instance().topLevelWidgets()
        widgets = widgets + QtWidgets.QApplication.instance().allWidgets()
        for x in widgets:
            if str(x.objectName()) == widget_name:
                return x


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = TaskBoard()
    window.show()
    app.exec_()
