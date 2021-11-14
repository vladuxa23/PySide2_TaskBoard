# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskBoard_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TaskBoard(object):
    def setupUi(self, TaskBoard):
        if not TaskBoard.objectName():
            TaskBoard.setObjectName(u"TaskBoard")
        TaskBoard.resize(731, 339)
        TaskBoard.setStyleSheet(u"QScrollArea {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.actionExit = QAction(TaskBoard)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(TaskBoard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollAreaDone = QScrollArea(self.centralwidget)
        self.scrollAreaDone.setObjectName(u"scrollAreaDone")
        self.scrollAreaDone.setMinimumSize(QSize(200, 280))
        self.scrollAreaDone.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 196, 276))
        self.scrollAreaDone.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout.addWidget(self.scrollAreaDone)

        self.scrollAreaDoing = QScrollArea(self.centralwidget)
        self.scrollAreaDoing.setObjectName(u"scrollAreaDoing")
        self.scrollAreaDoing.setMinimumSize(QSize(200, 280))
        self.scrollAreaDoing.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 196, 276))
        self.scrollAreaDoing.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout.addWidget(self.scrollAreaDoing)

        self.scrollAreaDo = QScrollArea(self.centralwidget)
        self.scrollAreaDo.setObjectName(u"scrollAreaDo")
        self.scrollAreaDo.setMinimumSize(QSize(200, 280))
        self.scrollAreaDo.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 196, 276))
        self.scrollAreaDo.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollAreaDo)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(72, 228, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        TaskBoard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TaskBoard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 731, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        TaskBoard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TaskBoard)
        self.statusbar.setObjectName(u"statusbar")
        TaskBoard.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionExit)

        self.retranslateUi(TaskBoard)

        QMetaObject.connectSlotsByName(TaskBoard)
    # setupUi

    def retranslateUi(self, TaskBoard):
        TaskBoard.setWindowTitle(QCoreApplication.translate("TaskBoard", u"TaskBoard", None))
        self.actionExit.setText(QCoreApplication.translate("TaskBoard", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton.setText(QCoreApplication.translate("TaskBoard", u"Add Task", None))
        self.menu.setTitle(QCoreApplication.translate("TaskBoard", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

