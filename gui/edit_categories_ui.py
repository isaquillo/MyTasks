# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_categories.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(230, 360)
        Dialog.setMinimumSize(QSize(230, 360))
        Dialog.setMaximumSize(QSize(230, 360))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 191, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listViewCategories = QListView(self.layoutWidget)
        self.listViewCategories.setObjectName(u"listViewCategories")
        self.listViewCategories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listViewCategories.setAlternatingRowColors(False)

        self.verticalLayout.addWidget(self.listViewCategories)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 270, 191, 46))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEditCategoryName = QLineEdit(self.layoutWidget1)
        self.lineEditCategoryName.setObjectName(u"lineEditCategoryName")

        self.verticalLayout_2.addWidget(self.lineEditCategoryName)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 220, 191, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDeleteCategory = QPushButton(self.layoutWidget2)
        self.pushButtonDeleteCategory.setObjectName(u"pushButtonDeleteCategory")

        self.horizontalLayout.addWidget(self.pushButtonDeleteCategory)

        self.pushButtonModifyCategory = QPushButton(self.layoutWidget2)
        self.pushButtonModifyCategory.setObjectName(u"pushButtonModifyCategory")

        self.horizontalLayout.addWidget(self.pushButtonModifyCategory)

        self.layoutWidget3 = QWidget(Dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 320, 191, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonCancel = QPushButton(self.layoutWidget3)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_2.addWidget(self.pushButtonCancel)

        self.pushButtonCreateCategory = QPushButton(self.layoutWidget3)
        self.pushButtonCreateCategory.setObjectName(u"pushButtonCreateCategory")

        self.horizontalLayout_2.addWidget(self.pushButtonCreateCategory)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit categories", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Current categories", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter new category", None))
        self.pushButtonDeleteCategory.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pushButtonModifyCategory.setText(QCoreApplication.translate("Dialog", u"Modify", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButtonCreateCategory.setText(QCoreApplication.translate("Dialog", u"Create", None))
    # retranslateUi

