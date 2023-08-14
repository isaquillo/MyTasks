# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_skin.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(290, 180)
        Dialog.setMinimumSize(QSize(290, 180))
        Dialog.setMaximumSize(QSize(290, 180))
        Dialog.setModal(False)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 271, 146))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonApply = QPushButton(self.widget)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.gridLayout.addWidget(self.pushButtonApply, 0, 1, 1, 1)

        self.pushButtonAccept = QPushButton(self.widget)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")

        self.gridLayout.addWidget(self.pushButtonAccept, 2, 1, 1, 1)

        self.pushButtonCancel = QPushButton(self.widget)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.gridLayout.addWidget(self.pushButtonCancel, 1, 1, 1, 1)

        self.listViewSkins = QListView(self.widget)
        self.listViewSkins.setObjectName(u"listViewSkins")

        self.gridLayout.addWidget(self.listViewSkins, 0, 0, 3, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.pushButtonApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.pushButtonAccept.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

