# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainbNkLau.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 630)
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
        self.stackedWidgetMain.setGeometry(QRect(0, 30, 1000, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidgetMain.sizePolicy().hasHeightForWidth())
        self.stackedWidgetMain.setSizePolicy(sizePolicy)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.gridLayout = QGridLayout(self.pageLogin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonLogin = QPushButton(self.pageLogin)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setMinimumSize(QSize(70, 40))
        self.pushButtonLogin.setMaximumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.pushButtonLogin, 5, 0, 1, 1, Qt.AlignHCenter)

        self.lineEditPassword = QLineEdit(self.pageLogin)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setMinimumSize(QSize(200, 40))
        self.lineEditPassword.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.lineEditPassword, 4, 0, 1, 1, Qt.AlignHCenter)

        self.labelLoginError = QLabel(self.pageLogin)
        self.labelLoginError.setObjectName(u"labelLoginError")
        self.labelLoginError.setStyleSheet(u"color: red;")
        self.labelLoginError.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoginError, 7, 0, 1, 1, Qt.AlignHCenter)

        self.pushButtonSignup = QPushButton(self.pageLogin)
        self.pushButtonSignup.setObjectName(u"pushButtonSignup")
        self.pushButtonSignup.setMinimumSize(QSize(70, 40))
        self.pushButtonSignup.setMaximumSize(QSize(70, 40))

        self.gridLayout.addWidget(self.pushButtonSignup, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.lineEditUsername = QLineEdit(self.pageLogin)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setMinimumSize(QSize(200, 40))
        self.lineEditUsername.setMaximumSize(QSize(200, 40))

        self.gridLayout.addWidget(self.lineEditUsername, 3, 0, 1, 1, Qt.AlignHCenter)

        self.label_7 = QLabel(self.pageLogin)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(288, 50))

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.stackedWidgetMain.addWidget(self.pageLogin)
        self.page_2Menu = QWidget()
        self.page_2Menu.setObjectName(u"page_2Menu")
        self.gridLayout_2 = QGridLayout(self.page_2Menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButtonFlightData = QPushButton(self.page_2Menu)
        self.pushButtonFlightData.setObjectName(u"pushButtonFlightData")

        self.gridLayout_2.addWidget(self.pushButtonFlightData, 0, 0, 2, 1)

        self.pushButtonConfig = QPushButton(self.page_2Menu)
        self.pushButtonConfig.setObjectName(u"pushButtonConfig")

        self.gridLayout_2.addWidget(self.pushButtonConfig, 0, 2, 2, 1)

        self.comboBoxBaudrate = QComboBox(self.page_2Menu)
        self.comboBoxBaudrate.setObjectName(u"comboBoxBaudrate")

        self.gridLayout_2.addWidget(self.comboBoxBaudrate, 1, 5, 1, 1)

        self.stackedWidgetMenu = QStackedWidget(self.page_2Menu)
        self.stackedWidgetMenu.setObjectName(u"stackedWidgetMenu")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.webEngineViewMap = QWebEngineView(self.page_3)
        self.webEngineViewMap.setObjectName(u"webEngineViewMap")
        self.webEngineViewMap.setGeometry(QRect(0, 0, 1000, 530))
        self.webEngineViewMap.setUrl(QUrl(u"about:blank"))
        self.pushButtonCurrentLocation = QPushButton(self.page_3)
        self.pushButtonCurrentLocation.setObjectName(u"pushButtonCurrentLocation")
        self.pushButtonCurrentLocation.setGeometry(QRect(10, 80, 50, 50))
        self.pushButtonCurrentLocation.setStyleSheet(u"font-size: 30px")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 211, 251, 251))
        self.tabWidget.setStyleSheet(u"color: black;")
        self.stats = QWidget()
        self.stats.setObjectName(u"stats")
        self.labelPlaneStatsDisplay = QLabel(self.stats)
        self.labelPlaneStatsDisplay.setObjectName(u"labelPlaneStatsDisplay")
        self.labelPlaneStatsDisplay.setGeometry(QRect(10, 10, 141, 201))
        self.labelPlaneStatsDisplay.setStyleSheet(u"color: white;")
        self.labelPlaneStats = QLabel(self.stats)
        self.labelPlaneStats.setObjectName(u"labelPlaneStats")
        self.labelPlaneStats.setGeometry(QRect(160, 10, 81, 201))
        self.labelPlaneStats.setStyleSheet(u"color: white;")
        self.labelPlaneStats.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelPlaneStats.setMargin(10)
        self.tabWidget.addTab(self.stats, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButtonMinimiseStats = QPushButton(self.page_3)
        self.pushButtonMinimiseStats.setObjectName(u"pushButtonMinimiseStats")
        self.pushButtonMinimiseStats.setGeometry(QRect(10, 460, 31, 31))
        self.stackedWidgetMenu.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 20, 121, 21))
        self.plot = QWidget(self.page_1)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(10, 50, 961, 431))
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

        self.gridLayout_2.addWidget(self.stackedWidgetMenu, 2, 0, 1, 8)

        self.comboBoxCom = QComboBox(self.page_2Menu)
        self.comboBoxCom.setObjectName(u"comboBoxCom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxCom.sizePolicy().hasHeightForWidth())
        self.comboBoxCom.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBoxCom, 0, 5, 1, 1)

        self.label = QLabel(self.page_2Menu)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_2.addWidget(self.label, 0, 4, 1, 1)

        self.pushButtonUpdateCOMports = QPushButton(self.page_2Menu)
        self.pushButtonUpdateCOMports.setObjectName(u"pushButtonUpdateCOMports")
        sizePolicy.setHeightForWidth(self.pushButtonUpdateCOMports.sizePolicy().hasHeightForWidth())
        self.pushButtonUpdateCOMports.setSizePolicy(sizePolicy)
        self.pushButtonUpdateCOMports.setMinimumSize(QSize(10, 0))
        self.pushButtonUpdateCOMports.setMaximumSize(QSize(100, 40))
        self.pushButtonUpdateCOMports.setStyleSheet(u"font-size:15px;")

        self.gridLayout_2.addWidget(self.pushButtonUpdateCOMports, 0, 6, 1, 1)

        self.pushButtonHelp = QPushButton(self.page_2Menu)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")

        self.gridLayout_2.addWidget(self.pushButtonHelp, 0, 3, 2, 1)

        self.label_2 = QLabel(self.page_2Menu)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 4, 1, 1)

        self.pushButtonConnectSerial = QPushButton(self.page_2Menu)
        self.pushButtonConnectSerial.setObjectName(u"pushButtonConnectSerial")
        sizePolicy.setHeightForWidth(self.pushButtonConnectSerial.sizePolicy().hasHeightForWidth())
        self.pushButtonConnectSerial.setSizePolicy(sizePolicy)
        self.pushButtonConnectSerial.setMinimumSize(QSize(10, 0))
        self.pushButtonConnectSerial.setMaximumSize(QSize(100, 40))
        self.pushButtonConnectSerial.setStyleSheet(u"font-size:15px;")

        self.gridLayout_2.addWidget(self.pushButtonConnectSerial, 1, 6, 1, 1)

        self.pushButtonSetup = QPushButton(self.page_2Menu)
        self.pushButtonSetup.setObjectName(u"pushButtonSetup")

        self.gridLayout_2.addWidget(self.pushButtonSetup, 0, 1, 2, 1)

        self.pushButtonSignOut = QPushButton(self.page_2Menu)
        self.pushButtonSignOut.setObjectName(u"pushButtonSignOut")
        sizePolicy.setHeightForWidth(self.pushButtonSignOut.sizePolicy().hasHeightForWidth())
        self.pushButtonSignOut.setSizePolicy(sizePolicy)
        self.pushButtonSignOut.setMinimumSize(QSize(10, 0))
        self.pushButtonSignOut.setMaximumSize(QSize(30, 30))
        self.pushButtonSignOut.setStyleSheet(u"font-size:15px;")

        self.gridLayout_2.addWidget(self.pushButtonSignOut, 0, 7, 1, 1)

        self.stackedWidgetMain.addWidget(self.page_2Menu)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEditPasswordNew = QLineEdit(self.page)
        self.lineEditPasswordNew.setObjectName(u"lineEditPasswordNew")
        self.lineEditPasswordNew.setMinimumSize(QSize(200, 40))
        self.lineEditPasswordNew.setMaximumSize(QSize(200, 40))

        self.gridLayout_3.addWidget(self.lineEditPasswordNew, 3, 3, 1, 1)

        self.lineEditEmailNew = QLineEdit(self.page)
        self.lineEditEmailNew.setObjectName(u"lineEditEmailNew")
        self.lineEditEmailNew.setMinimumSize(QSize(200, 40))
        self.lineEditEmailNew.setMaximumSize(QSize(200, 40))

        self.gridLayout_3.addWidget(self.lineEditEmailNew, 2, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 11, 3, 2, 1)

        self.lineEditUsernameNew = QLineEdit(self.page)
        self.lineEditUsernameNew.setObjectName(u"lineEditUsernameNew")
        self.lineEditUsernameNew.setMinimumSize(QSize(200, 40))
        self.lineEditUsernameNew.setMaximumSize(QSize(200, 40))

        self.gridLayout_3.addWidget(self.lineEditUsernameNew, 1, 3, 1, 1)

        self.pushButtonSignupNew = QPushButton(self.page)
        self.pushButtonSignupNew.setObjectName(u"pushButtonSignupNew")
        self.pushButtonSignupNew.setMinimumSize(QSize(70, 40))
        self.pushButtonSignupNew.setMaximumSize(QSize(70, 40))

        self.gridLayout_3.addWidget(self.pushButtonSignupNew, 7, 3, 1, 1, Qt.AlignHCenter)

        self.pushButtonBackToLogin = QPushButton(self.page)
        self.pushButtonBackToLogin.setObjectName(u"pushButtonBackToLogin")
        sizePolicy.setHeightForWidth(self.pushButtonBackToLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonBackToLogin.setSizePolicy(sizePolicy)
        self.pushButtonBackToLogin.setMinimumSize(QSize(70, 40))
        self.pushButtonBackToLogin.setMaximumSize(QSize(70, 40))

        self.gridLayout_3.addWidget(self.pushButtonBackToLogin, 8, 3, 1, 1, Qt.AlignHCenter)

        self.stackedWidgetMain.addWidget(self.page)
        self.frameHeader = QFrame(self.centralwidget)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setGeometry(QRect(0, 0, 1000, 30))
        self.frameHeader.setFrameShape(QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frameHeader)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(427, 10, 144, 24))
        self.label_10.setMaximumSize(QSize(288, 50))
        self.labelVersion = QLabel(self.frameHeader)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setGeometry(QRect(20, 10, 281, 21))
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.labelVersion.setFont(font)
        self.labelVersion.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButtonExit = QPushButton(self.frameHeader)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        self.pushButtonExit.setGeometry(QRect(970, 0, 31, 30))
        self.pushButtonExit.setAutoFillBackground(False)
        self.pushButtonExit.setStyleSheet(u"background-color: #222222;")
        icon1 = QIcon()
        icon1.addFile(u"img/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonExit.setIcon(icon1)
        self.pushButtonExit.setIconSize(QSize(24, 24))
        self.pushButtonMinimise = QPushButton(self.frameHeader)
        self.pushButtonMinimise.setObjectName(u"pushButtonMinimise")
        self.pushButtonMinimise.setGeometry(QRect(940, 0, 31, 30))
        self.pushButtonMinimise.setAutoFillBackground(False)
        self.pushButtonMinimise.setStyleSheet(u"background-color: #222222;")
        icon2 = QIcon()
        icon2.addFile(u"img/minimize-window-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMinimise.setIcon(icon2)
        self.pushButtonMinimise.setIconSize(QSize(24, 24))
        self.pushButtonMinimise.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButtonLogin, self.pushButtonFlightData)
        QWidget.setTabOrder(self.pushButtonFlightData, self.pushButtonSetup)
        QWidget.setTabOrder(self.pushButtonSetup, self.pushButtonConfig)
        QWidget.setTabOrder(self.pushButtonConfig, self.pushButtonHelp)
        QWidget.setTabOrder(self.pushButtonHelp, self.comboBoxCom)
        QWidget.setTabOrder(self.comboBoxCom, self.pushButtonCurrentLocation)
        QWidget.setTabOrder(self.pushButtonCurrentLocation, self.comboBoxBaudrate)
        QWidget.setTabOrder(self.comboBoxBaudrate, self.pushButtonSignup)
        QWidget.setTabOrder(self.pushButtonSignup, self.lineEditUsernameNew)
        QWidget.setTabOrder(self.lineEditUsernameNew, self.lineEditEmailNew)
        QWidget.setTabOrder(self.lineEditEmailNew, self.lineEditPasswordNew)
        QWidget.setTabOrder(self.lineEditPasswordNew, self.lineEditUsername)
        QWidget.setTabOrder(self.lineEditUsername, self.pushButtonSignupNew)
        QWidget.setTabOrder(self.pushButtonSignupNew, self.lineEditPassword)

        self.retranslateUi(MainWindow)

        self.stackedWidgetMain.setCurrentIndex(1)
        self.stackedWidgetMenu.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AvASys Controller", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.labelLoginError.setText(QCoreApplication.translate("MainWindow", u"Incorrect Username/Password", None))
        self.pushButtonSignup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/img/logoSmall.png\"/></p></body></html>", None))
        self.pushButtonFlightData.setText(QCoreApplication.translate("MainWindow", u"Flight Data", None))
        self.pushButtonConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.pushButtonCurrentLocation.setText(QCoreApplication.translate("MainWindow", u"\u25ce", None))
        self.labelPlaneStatsDisplay.setText("")
        self.labelPlaneStats.setText(QCoreApplication.translate("MainWindow", u"<html><head/>\n"
"<body>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"<p><span style=\" font-size:11pt;\">0</span></p>\n"
"</body>\n"
"</html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stats), QCoreApplication.translate("MainWindow", u"Stats", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Other", None))
        self.pushButtonMinimiseStats.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Flight data page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Setup page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Config page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Help page", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Com", None))
        self.pushButtonUpdateCOMports.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate", None))
        self.pushButtonConnectSerial.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButtonSetup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.pushButtonSignOut.setText(QCoreApplication.translate("MainWindow", u"\u2300", None))
        self.lineEditPasswordNew.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.lineEditEmailNew.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEditUsernameNew.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Username", None))
        self.pushButtonSignupNew.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.pushButtonBackToLogin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/img/logoSmall.png\" width=\"144\" height=\"24\"></p></body></html>", None))
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">AvASys v1.2.1</span></p></body></html>", None))
        self.pushButtonExit.setText("")
        self.pushButtonMinimise.setText("")
    # retranslateUi

