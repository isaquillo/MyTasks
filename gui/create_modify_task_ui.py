# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_modify_task.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 420)
        Dialog.setMinimumSize(QSize(370, 420))
        Dialog.setMaximumSize(QSize(370, 420))
        Dialog.setModal(True)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 351, 391))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 110, 49, 16))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(32, 206, 61, 171))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 205, 135, 181))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dateEditStartDate = QDateEdit(self.layoutWidget1)
        self.dateEditStartDate.setObjectName(u"dateEditStartDate")
        self.dateEditStartDate.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEditStartDate)

        self.dateEditEndDate = QDateEdit(self.layoutWidget1)
        self.dateEditEndDate.setObjectName(u"dateEditEndDate")
        self.dateEditEndDate.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEditEndDate)

        self.comboBoxCategory = QComboBox(self.layoutWidget1)
        self.comboBoxCategory.setObjectName(u"comboBoxCategory")

        self.verticalLayout_2.addWidget(self.comboBoxCategory)

        self.pushButtonManageCategories = QPushButton(self.layoutWidget1)
        self.pushButtonManageCategories.setObjectName(u"pushButtonManageCategories")

        self.verticalLayout_2.addWidget(self.pushButtonManageCategories)

        self.comboBoxPercentage = QComboBox(self.layoutWidget1)
        self.comboBoxPercentage.addItem("")
        self.comboBoxPercentage.addItem("")
        self.comboBoxPercentage.addItem("")
        self.comboBoxPercentage.addItem("")
        self.comboBoxPercentage.addItem("")
        self.comboBoxPercentage.setObjectName(u"comboBoxPercentage")

        self.verticalLayout_2.addWidget(self.comboBoxPercentage)

        self.lineEditOwner = QLineEdit(self.layoutWidget1)
        self.lineEditOwner.setObjectName(u"lineEditOwner")

        self.verticalLayout_2.addWidget(self.lineEditOwner)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(23, 24, 311, 171))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEditName = QLineEdit(self.layoutWidget2)
        self.lineEditName.setObjectName(u"lineEditName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditName)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.textEditDescription = QTextEdit(self.layoutWidget2)
        self.textEditDescription.setObjectName(u"textEditDescription")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEditDescription)

        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(248, 317, 91, 61))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButtonCancel = QPushButton(self.layoutWidget3)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.verticalLayout_3.addWidget(self.pushButtonCancel)

        self.pushButtonSave = QPushButton(self.layoutWidget3)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.verticalLayout_3.addWidget(self.pushButtonSave)


        self.retranslateUi(Dialog)

        self.comboBoxCategory.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.groupBox.setTitle("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Start Date", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"End Date", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.label_9.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Percentage", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Owner", None))
        self.dateEditStartDate.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.dateEditEndDate.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd-MM-yyyy", None))
        self.pushButtonManageCategories.setText(QCoreApplication.translate("Dialog", u"Manage categories...", None))
        self.comboBoxPercentage.setItemText(0, QCoreApplication.translate("Dialog", u"0 %", None))
        self.comboBoxPercentage.setItemText(1, QCoreApplication.translate("Dialog", u"25 %", None))
        self.comboBoxPercentage.setItemText(2, QCoreApplication.translate("Dialog", u"50 %", None))
        self.comboBoxPercentage.setItemText(3, QCoreApplication.translate("Dialog", u"75 %", None))
        self.comboBoxPercentage.setItemText(4, QCoreApplication.translate("Dialog", u"100 %", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

