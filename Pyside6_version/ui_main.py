# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjBymOT.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.lineEditUsername.setMinimumSize(QSize(200, 35))
        self.lineEditUsername.setMaximumSize(QSize(200, 35))

        self.gridLayout.addWidget(self.lineEditUsername, 3, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.pushButtonLogin = QPushButton(self.pageLogin)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setMinimumSize(QSize(70, 35))
        self.pushButtonLogin.setMaximumSize(QSize(70, 35))

        self.gridLayout.addWidget(self.pushButtonLogin, 5, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.lineEditPassword = QLineEdit(self.pageLogin)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setMinimumSize(QSize(200, 35))
        self.lineEditPassword.setMaximumSize(QSize(200, 35))

        self.gridLayout.addWidget(self.lineEditPassword, 4, 0, 1, 1, Qt.AlignHCenter)

        self.pushButtonSignup = QPushButton(self.pageLogin)
        self.pushButtonSignup.setObjectName(u"pushButtonSignup")
        self.pushButtonSignup.setMinimumSize(QSize(70, 35))
        self.pushButtonSignup.setMaximumSize(QSize(70, 35))

        self.gridLayout.addWidget(self.pushButtonSignup, 6, 0, 1, 1, Qt.AlignHCenter)

        self.labelLoginError = QLabel(self.pageLogin)
        self.labelLoginError.setObjectName(u"labelLoginError")
        self.labelLoginError.setStyleSheet(u"color: red;")
        self.labelLoginError.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoginError, 7, 0, 1, 1, Qt.AlignHCenter)

        self.label_7 = QLabel(self.pageLogin)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(288, 50))

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageLogin)
        self.page_2Menu = QWidget()
        self.page_2Menu.setObjectName(u"page_2Menu")
        self.gridLayout_2 = QGridLayout(self.page_2Menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.page_2Menu)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 4, 1, 1)

        self.pushButtonFlightData = QPushButton(self.page_2Menu)
        self.pushButtonFlightData.setObjectName(u"pushButtonFlightData")

        self.gridLayout_2.addWidget(self.pushButtonFlightData, 0, 0, 2, 1)

        self.stackedWidgetMenu = QStackedWidget(self.page_2Menu)
        self.stackedWidgetMenu.setObjectName(u"stackedWidgetMenu")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.webEngineViewMap = QWebEngineView(self.page_3)
        self.webEngineViewMap.setObjectName(u"webEngineViewMap")
        self.webEngineViewMap.setGeometry(QRect(0, 0, 1000, 530))
        self.webEngineViewMap.setUrl(QUrl(u"about:blank"))
        self.pushButtonMapZoomIn = QPushButton(self.page_3)
        self.pushButtonMapZoomIn.setObjectName(u"pushButtonMapZoomIn")
        self.pushButtonMapZoomIn.setGeometry(QRect(10, 20, 50, 50))
        self.pushButtonMapZoomOut = QPushButton(self.page_3)
        self.pushButtonMapZoomOut.setObjectName(u"pushButtonMapZoomOut")
        self.pushButtonMapZoomOut.setGeometry(QRect(10, 80, 50, 50))
        self.pushButtonCurrentLocation = QPushButton(self.page_3)
        self.pushButtonCurrentLocation.setObjectName(u"pushButtonCurrentLocation")
        self.pushButtonCurrentLocation.setGeometry(QRect(10, 140, 50, 50))
        self.stackedWidgetMenu.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 200, 121, 21))
        self.stackedWidgetMenu.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 200, 121, 21))
        self.stackedWidgetMenu.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 200, 121, 21))
        self.stackedWidgetMenu.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 200, 121, 21))
        self.stackedWidgetMenu.addWidget(self.page_5)

        self.gridLayout_2.addWidget(self.stackedWidgetMenu, 2, 0, 1, 6)

        self.pushButtonSetup = QPushButton(self.page_2Menu)
        self.pushButtonSetup.setObjectName(u"pushButtonSetup")

        self.gridLayout_2.addWidget(self.pushButtonSetup, 0, 1, 2, 1)

        self.comboBoxSerial = QComboBox(self.page_2Menu)
        self.comboBoxSerial.setObjectName(u"comboBoxSerial")

        self.gridLayout_2.addWidget(self.comboBoxSerial, 1, 5, 1, 1)

        self.label_2 = QLabel(self.page_2Menu)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 4, 1, 1)

        self.pushButtonConfig = QPushButton(self.page_2Menu)
        self.pushButtonConfig.setObjectName(u"pushButtonConfig")

        self.gridLayout_2.addWidget(self.pushButtonConfig, 0, 2, 2, 1)

        self.comboBoxComm = QComboBox(self.page_2Menu)
        self.comboBoxComm.setObjectName(u"comboBoxComm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxComm.sizePolicy().hasHeightForWidth())
        self.comboBoxComm.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBoxComm, 0, 5, 1, 1)

        self.pushButtonHelp = QPushButton(self.page_2Menu)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")

        self.gridLayout_2.addWidget(self.pushButtonHelp, 0, 3, 2, 1)

        self.stackedWidgetMain.addWidget(self.page_2Menu)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 224, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.lineEditUsernameNew = QLineEdit(self.page)
        self.lineEditUsernameNew.setObjectName(u"lineEditUsernameNew")
        self.lineEditUsernameNew.setMaximumSize(QSize(200, 35))

        self.gridLayout_3.addWidget(self.lineEditUsernameNew, 1, 1, 1, 1)

        self.lineEditPasswordNew = QLineEdit(self.page)
        self.lineEditPasswordNew.setObjectName(u"lineEditPasswordNew")
        self.lineEditPasswordNew.setMaximumSize(QSize(200, 35))

        self.gridLayout_3.addWidget(self.lineEditPasswordNew, 2, 1, 1, 1)

        self.pushButtonSignupNew = QPushButton(self.page)
        self.pushButtonSignupNew.setObjectName(u"pushButtonSignupNew")
        self.pushButtonSignupNew.setMaximumSize(QSize(70, 35))

        self.gridLayout_3.addWidget(self.pushButtonSignupNew, 4, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.stackedWidgetMain.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        QWidget.setTabOrder(self.lineEditPassword, self.pushButtonLogin)
        QWidget.setTabOrder(self.pushButtonLogin, self.pushButtonFlightData)
        QWidget.setTabOrder(self.pushButtonFlightData, self.pushButtonSetup)
        QWidget.setTabOrder(self.pushButtonSetup, self.pushButtonConfig)
        QWidget.setTabOrder(self.pushButtonConfig, self.pushButtonHelp)
        QWidget.setTabOrder(self.pushButtonHelp, self.pushButtonMapZoomIn)
        QWidget.setTabOrder(self.pushButtonMapZoomIn, self.comboBoxComm)
        QWidget.setTabOrder(self.comboBoxComm, self.pushButtonMapZoomOut)
        QWidget.setTabOrder(self.pushButtonMapZoomOut, self.pushButtonCurrentLocation)
        QWidget.setTabOrder(self.pushButtonCurrentLocation, self.comboBoxSerial)

        self.retranslateUi(MainWindow)

        self.stackedWidgetMain.setCurrentIndex(0)
        self.stackedWidgetMenu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AvASys v1.2", None))
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButtonSignup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.labelLoginError.setText(QCoreApplication.translate("MainWindow", u"Incorrect Username/Password", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/img/logoSmall.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Comm", None))
        self.pushButtonFlightData.setText(QCoreApplication.translate("MainWindow", u"Flight Data", None))
        self.pushButtonMapZoomIn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButtonMapZoomOut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButtonCurrentLocation.setText(QCoreApplication.translate("MainWindow", u"\u2302", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Flight data page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Setup page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Config page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Help page", None))
        self.pushButtonSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.pushButtonConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.lineEditUsernameNew.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEditPasswordNew.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButtonSignupNew.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi

