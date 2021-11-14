import sys
from PySide2 import QtCore, QtWidgets, QtGui


class TaskWidget(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(TaskWidget, self).__init__(parent)
        self.setWindowFlag(QtGui.Qt.FramelessWindowHint)
        # self.setAttribute(QtGui.Qt.WA_TranslucentBackground, True)
        self.setMinimumHeight(100)
        # self.setMinimumSize(100, 100)
        # self.setMaximumHeight(100)

        self.setStyleSheet("""
        border: 1px solid black;
        border-radius: 5px;
        background: #002025;
        """)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = TaskWidget()
    window.show()
    sys.exit(app.exec_())
