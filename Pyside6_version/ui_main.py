# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainsYypZc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border: 1px solid #444444;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"    border: 1px solid #444444;\n"
"    padding: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidgetMain = QStackedWidget(self.centralwidget)
        self.stackedWidgetMain.setObjectName(u"stackedWidgetMain")
        self.stackedWidgetMain.setGeometry(QRect(0, 0, 1000, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidgetMain.sizePolicy().hasHeightForWidth())
        self.stackedWidgetMain.setSizePolicy(sizePolicy)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.gridLayout = QGridLayout(self.pageLogin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEditUsername = QLineEdit(self.pageLogin)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setMaximumSize(QSize(200, 35))

        self.gridLayout.addWidget(self.lineEditUsername, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.pushButtonLogin = QPushButton(self.pageLogin)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setMaximumSize(QSize(70, 35))

        self.gridLayout.addWidget(self.pushButtonLogin, 5, 0, 1, 1, Qt.AlignHCenter)

        self.lineEditPassword = QLineEdit(self.pageLogin)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setMaximumSize(QSize(200, 35))

        self.gridLayout.addWidget(self.lineEditPassword, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageLogin)
        self.page_2Menu = QWidget()
        self.page_2Menu.setObjectName(u"page_2Menu")
        self.gridLayout_2 = QGridLayout(self.page_2Menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidgetMenu = QStackedWidget(self.page_2Menu)
        self.stackedWidgetMenu.setObjectName(u"stackedWidgetMenu")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.webEngineViewMap = QWebEngineView(self.page_3)
        self.webEngineViewMap.setObjectName(u"webEngineViewMap")
        self.webEngineViewMap.setGeometry(QRect(0, 0, 1000, 530))
        self.webEngineViewMap.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetMenu.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidgetMenu, 2, 0, 1, 4)

        self.pushButton_3 = QPushButton(self.page_2Menu)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.page_2Menu)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.page_2Menu)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.page_2Menu)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.stackedWidgetMain.addWidget(self.page_2Menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidgetMain.setCurrentIndex(1)
        self.stackedWidgetMenu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AvASys v1.2", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

