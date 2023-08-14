# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        MainWindow.setMaximumSize(QSize(900, 500))
        MainWindow.setStyleSheet(u"")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad_previous_state = QAction(MainWindow)
        self.actionLoad_previous_state.setObjectName(u"actionLoad_previous_state")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        self.actionChange_skin = QAction(MainWindow)
        self.actionChange_skin.setObjectName(u"actionChange_skin")
        self.actionCategories = QAction(MainWindow)
        self.actionCategories.setObjectName(u"actionCategories")
        self.actionChangeSkin = QAction(MainWindow)
        self.actionChangeSkin.setObjectName(u"actionChangeSkin")
        self.actionLoadNewSkin = QAction(MainWindow)
        self.actionLoadNewSkin.setObjectName(u"actionLoadNewSkin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 861, 381))
        self.tableViewTasks = QTableView(self.groupBox)
        self.tableViewTasks.setObjectName(u"tableViewTasks")
        self.tableViewTasks.setGeometry(QRect(10, 10, 841, 361))
        self.tableViewTasks.setFocusPolicy(Qt.NoFocus)
        self.tableViewTasks.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableViewTasks.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableViewTasks.setDragDropOverwriteMode(False)
        self.tableViewTasks.setAlternatingRowColors(False)
        self.tableViewTasks.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewTasks.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableViewTasks.setSortingEnabled(True)
        self.tableViewTasks.verticalHeader().setVisible(False)
        self.tableViewTasks.verticalHeader().setHighlightSections(False)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(360, 410, 521, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDelete = QPushButton(self.layoutWidget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.pushButtonModify = QPushButton(self.layoutWidget)
        self.pushButtonModify.setObjectName(u"pushButtonModify")

        self.horizontalLayout.addWidget(self.pushButtonModify)

        self.pushButtonCreate = QPushButton(self.layoutWidget)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")

        self.horizontalLayout.addWidget(self.pushButtonCreate)

        self.checkBoxCompletedTasks = QCheckBox(self.centralwidget)
        self.checkBoxCompletedTasks.setObjectName(u"checkBoxCompletedTasks")
        self.checkBoxCompletedTasks.setGeometry(QRect(180, 410, 151, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionChangeSkin)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Tasks", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad_previous_state.setText(QCoreApplication.translate("MainWindow", u"Load previous state", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.actionManual.setText(QCoreApplication.translate("MainWindow", u"Manual...", None))
        self.actionChange_skin.setText(QCoreApplication.translate("MainWindow", u"Change skin...", None))
        self.actionCategories.setText(QCoreApplication.translate("MainWindow", u"Categories...", None))
        self.actionChangeSkin.setText(QCoreApplication.translate("MainWindow", u"Change skin...", None))
        self.actionLoadNewSkin.setText(QCoreApplication.translate("MainWindow", u"Load new skin...", None))
        self.groupBox.setTitle("")
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButtonModify.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.checkBoxCompletedTasks.setText(QCoreApplication.translate("MainWindow", u"Show completed tasks", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

