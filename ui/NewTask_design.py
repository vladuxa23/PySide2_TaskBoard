# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewTask_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewTaskForm(object):
    def setupUi(self, NewTaskForm):
        if not NewTaskForm.objectName():
            NewTaskForm.setObjectName(u"NewTaskForm")
        NewTaskForm.resize(300, 350)
        NewTaskForm.setMinimumSize(QSize(300, 350))
        NewTaskForm.setMaximumSize(QSize(400, 450))
        self.verticalLayout = QVBoxLayout(NewTaskForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelCategory = QLabel(NewTaskForm)
        self.labelCategory.setObjectName(u"labelCategory")

        self.verticalLayout.addWidget(self.labelCategory)

        self.comboBoxCategory = QComboBox(NewTaskForm)
        self.comboBoxCategory.setObjectName(u"comboBoxCategory")

        self.verticalLayout.addWidget(self.comboBoxCategory)

        self.labelDoer = QLabel(NewTaskForm)
        self.labelDoer.setObjectName(u"labelDoer")

        self.verticalLayout.addWidget(self.labelDoer)

        self.comboBoxDoer = QComboBox(NewTaskForm)
        self.comboBoxDoer.setObjectName(u"comboBoxDoer")

        self.verticalLayout.addWidget(self.comboBoxDoer)

        self.labelTaskName = QLabel(NewTaskForm)
        self.labelTaskName.setObjectName(u"labelTaskName")

        self.verticalLayout.addWidget(self.labelTaskName)

        self.lineEditTaskName = QLineEdit(NewTaskForm)
        self.lineEditTaskName.setObjectName(u"lineEditTaskName")

        self.verticalLayout.addWidget(self.lineEditTaskName)

        self.labelDescription = QLabel(NewTaskForm)
        self.labelDescription.setObjectName(u"labelDescription")

        self.verticalLayout.addWidget(self.labelDescription)

        self.plainTextEditDescription = QPlainTextEdit(NewTaskForm)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")

        self.verticalLayout.addWidget(self.plainTextEditDescription)

        self.labelDateEnd = QLabel(NewTaskForm)
        self.labelDateEnd.setObjectName(u"labelDateEnd")

        self.verticalLayout.addWidget(self.labelDateEnd)

        self.dateEditEnd = QDateEdit(NewTaskForm)
        self.dateEditEnd.setObjectName(u"dateEditEnd")
        self.dateEditEnd.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEditEnd)

        self.pushButton = QPushButton(NewTaskForm)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(NewTaskForm)

        QMetaObject.connectSlotsByName(NewTaskForm)
    # setupUi

    def retranslateUi(self, NewTaskForm):
        NewTaskForm.setWindowTitle(QCoreApplication.translate("NewTaskForm", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.labelCategory.setText(QCoreApplication.translate("NewTaskForm", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.labelDoer.setText(QCoreApplication.translate("NewTaskForm", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c:", None))
        self.labelTaskName.setText(QCoreApplication.translate("NewTaskForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.labelDescription.setText(QCoreApplication.translate("NewTaskForm", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.labelDateEnd.setText(QCoreApplication.translate("NewTaskForm", u"\u0414\u0430\u0442\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.pushButton.setText(QCoreApplication.translate("NewTaskForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

