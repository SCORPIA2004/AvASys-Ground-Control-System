import re
import io
import sys
import csv
import json
import folium
import os.path
import serialCom
from ui_main import Ui_MainWindow
from emailSender import sendEmail
from urllib.request import urlopen
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication



class MainWindow(QMainWindow):

    # initialise the window with all widgets
    def __init__(self):
        # Initialising the window geometry
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.m = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ""
        self.password = ""
        self.email = ""
        self.dragPos = 0
        self.zoomScale = 100
        self.showMap()

        # Start window at Login page
        self.ui.stackedWidgetMain.setCurrentIndex(0)
        self.ui.labelLoginError.setText("")

        # Start assigning functions to login page widgets here
        self.ui.pushButtonLogin.clicked.connect(self.logUserIn)
        self.ui.lineEditUsername.textChanged.connect(self.setUsername)
        self.ui.lineEditPassword.textChanged.connect(self.setPassword)
        self.ui.pushButtonSignup.clicked.connect(self.signUpUser)
        self.ui.pushButtonSignupNew.clicked.connect(self.finishSigningUp)
        self.ui.lineEditUsernameNew.textChanged.connect(self.setUsername)
        self.ui.lineEditPasswordNew.textChanged.connect(self.setPassword)
        self.ui.lineEditEmailNew.textChanged.connect(self.setEmail)
        self.ui.pushButtonExit.clicked.connect(QCoreApplication.instance().quit)
        self.ui.pushButtonMinimise.clicked.connect(self.minimise)
        self.ui.frameHeader.mouseMoveEvent = self.moveWindow


        # start assigning functions to menu page widgets here
        self.ui.pushButtonFlightData.clicked.connect(self.gotoFlightDataPage)
        self.ui.pushButtonSetup.clicked.connect(self.gotoSetupPage)
        self.ui.pushButtonConfig.clicked.connect(self.gotoConfigPage)
        self.ui.pushButtonHelp.clicked.connect(self.gotoHelpPage)

        # start assigning functions to map page widgets here
        self.ui.pushButtonMinimiseStats.clicked.connect(self.minimiseStats)
        self.ui.pushButtonSignOut.clicked.connect(self.signOut)


        # COM ports stuff
        self.portManager = serialCom.COM()
        self.openPorts = self.portManager.getSerialPorts()
        self.bauds = ["300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400",
                      "57600", "115200"]




    def logUserIn(self):
        # open csv file
        # check if credentials.csv exists

        if not os.path.exists('credentials.csv'):
            # create credentials.csv
            with open('credentials.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "password"])
                self.ui.labelLoginError.setText("No users exist")
                file.close()


        with open('credentials.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # loop over the rows in the csv file

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if self.username == row[0] and self.password == row[1]:
                        # successful login redirect to menu page
                        self.ui.stackedWidgetMain.setCurrentIndex(1)
                        self.ui.stackedWidgetMenu.setCurrentIndex(0)
                        # show map here, instead of starting, to minimise loading time
                        self.showMap()
                    elif self.username != row[0] and self.password != row[1]:
                        self.ui.labelLoginError.setText("Wrong Username or Password")
                    elif self.username == row[0] and self.password != row[1]:
                        self.ui.labelLoginError.setText("Wrong Password")
                    elif self.username != row[0] and self.password == row[1]:
                        # if no such user exists, show error message
                        self.ui.labelLoginError.setText("Wrong Username")
                line_count += 1


        csv_file.close()

    def signOut(self):
        self.ui.stackedWidgetMain.setCurrentIndex(0)
        self.ui.labelLoginError.setText("Signed Out")

    def signUpUser(self):
        self.ui.stackedWidgetMain.setCurrentIndex(2)

    def is_valid_gmail(self):
        # Regular expression pattern for Gmail addresses
        # pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com$'
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        return re.match(pattern, self.email)

    def finishSigningUp(self):
        # open credentials.csv file for writing
        with open('credentials.csv', mode='a', newline='') as credentials_file:
            credentials_writer = csv.writer(credentials_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # write username and password to credentials.csv file
            credentials_writer.writerow([self.username, self.password])
        credentials_file.close()
        if self.is_valid_gmail():
            sendEmail(self.email)
        else:
            print("Invalid email address")
        self.ui.stackedWidgetMain.setCurrentIndex(0)

    def setUsername(self, s):
        self.username = s

    def setPassword(self, s):
        self.password = s

    def setEmail(self, s):
        self.email = s

    def minimiseStats(self):
        if self.ui.pushButtonMinimiseStats.text() == "-":
            self.ui.pushButtonMinimiseStats.setText("+")
            self.ui.tabWidget.hide()
        else:
            self.ui.pushButtonMinimiseStats.setText("-")
            self.ui.tabWidget.show()

    def showMap(self):
        # initialise coordiante variable
        self.coordinate = (0, 0)
        self.getCurrentCoordinates()

        # initialise map
        self.m = folium.Map(
            title="Flight Map",
            zoom_start=self.zoomScale,
            location=self.coordinate,
            zoom_control=True,
            # tiles = "Stamen Terrain",
        )

        # place plane marker on map
        folium.Marker(
            location=self.coordinate,
            popup="Plane " + str(self.coordinate),
            icon=folium.CustomIcon(icon_image="./img/plane.png", icon_size=(50, 50))
        ).add_to(self.m)

        # TESTING
        # Bind the click event to the map
        marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")
        self.m.add_child(marker)
        # self.m.add_child(folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"))
        # END TESTING

        # Coordinates of restricted fly zones
        zones = [
            {"name": "Esenboğa International Airport", "latitude": 40.1167, "longitude": 32.9950},
            {"name": "Etimesgut Air Base", "latitude": 39.9494, "longitude": 32.6833},
            {"name": "Akıncı Air Base", "latitude": 40.1397, "longitude": 32.5739}
        ]
        for zone in zones:
            folium.Circle(
                location=[zone["latitude"], zone["longitude"]],
                radius=2000,  # Adjust the radius as needed
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.3,
                tooltip=zone["name"]
            ).add_to(self.m)

        # saves map as html
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        html_content = data.getvalue().decode()
        # self.m.get_root().script.get_root().render()

        # displays map on webEngineViewMap widget in window
        self.ui.webEngineViewMap.setHtml(html_content)

    def gotoFlightDataPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(0)

    def gotoSetupPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(2)

    def gotoConfigPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(3)

    def gotoHelpPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(4)

    def getCurrentCoordinates(self):

        try:
            urlopen("http://ipinfo.io/json")
            data = json.load(urlopen("http://ipinfo.io/json"))
        except:
            print("No internet connection")
            return
        lat = data['loc'].split(',')[0]
        lon = data['loc'].split(',')[1]

        # print(lat, lon)
        self.coordinate = (float(lat), float(lon))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        if(True):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

    def minimise(self):
        self.showMinimized()

    def getPortFromCombo(self, event):
        self.portManager.setSerialPort(event)
        self.port = event

    def getBaudFromCombo(self, event):
        self.portManager.setBaudRate(event)
        self.baud = int(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())