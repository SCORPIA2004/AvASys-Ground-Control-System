import re
import io
import sys
import csv
import json
import folium
import os.path
import threading
import serial.tools.list_ports
from PySide6 import QtCore

from ui_main import Ui_MainWindow
from emailSender import sendEmail
from urllib.request import urlopen
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox


class MainWindow(QMainWindow):

    # initialise the window with all widgets
    def __init__(self, version):
        # Initialising the window geometry
        super(MainWindow, self).__init__()
        self.lonDir = None
        self.latDir = None
        self.longitudeConv = None
        self.latitudeConv = None
        self.serialThread = None
        self.longitude = None
        self.latitude = None
        self.markerLayer = None
        self.coordinate = None
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.m = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ""
        self.password = ""
        self.email = ""
        self.dragPos = 0
        self.zoomScale = 15
        self.selectedPort = ""
        self.selectedBaud = -1
        self.planeMarker = None


        # Serial stuff
        self.serialInst = serial.Serial()
        self.ports = serial.tools.list_ports.comports()
        self.portsList = []
        # for the COM ports list
        for port in self.ports:
            self.portsList.append(str(port))
        self.ui.comboBoxCom.addItems(self.portsList)

        # for the Serial bauds list
        self.bauds = ["300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400",
                      "57600", "115200"]
        self.ui.comboBoxBaudrate.addItems(self.bauds)

        self.showMap()

        # Start window at Login page
        self.ui.stackedWidgetMain.setCurrentIndex(0)
        self.ui.labelLoginError.setText("")
        self.ui.labelVersion.setText(version)

        # Start assigning functions to login page widgets here
        self.ui.pushButtonLogin.clicked.connect(self.logUserIn)
        self.ui.lineEditUsername.textChanged.connect(self.setUsername)
        self.ui.lineEditPassword.textChanged.connect(self.setPassword)
        self.ui.pushButtonSignup.clicked.connect(self.signUpUser)
        self.ui.pushButtonSignupNew.clicked.connect(self.finishSigningUp)
        self.ui.lineEditUsernameNew.textChanged.connect(self.setUsername)
        self.ui.lineEditPasswordNew.textChanged.connect(self.setPassword)
        self.ui.lineEditEmailNew.textChanged.connect(self.setEmail)
        self.ui.pushButtonBackToLogin.clicked.connect(self.backToLogin)
        self.ui.pushButtonExit.clicked.connect(self.exitApp)
        self.ui.pushButtonMinimise.clicked.connect(self.minimise)
        self.ui.frameHeader.mouseMoveEvent = self.moveWindow
        self.ui.pushButtonUpdateCOMports.clicked.connect(self.updateComPorts)
        self.ui.pushButtonConnectSerial.clicked.connect(self.connectSerial)
        self.ui.comboBoxCom.currentIndexChanged.connect(self.setPortFromComboBox)
        self.ui.comboBoxBaudrate.currentIndexChanged.connect(self.setBaudFromComboBox)
        self.ui.labelPlaneStatsDisplay.setText("Latitude:\n\nLongitude:\n\nAltitude:\n\nGroundspeed(m/s):\n\nAngle (deg):")
        self.ui.labelPlaneStats.setText("N/A\n\nN/A\n\nN/A\n\nN/A\n\nN/A")

        self.ui.pushButtonCurrentLocation.hide()

        # start assigning functions to menu page widgets here
        self.ui.pushButtonFlightData.clicked.connect(self.gotoFlightDataPage)
        self.ui.pushButtonSetup.clicked.connect(self.gotoSetupPage)
        self.ui.pushButtonConfig.clicked.connect(self.gotoConfigPage)
        self.ui.pushButtonHelp.clicked.connect(self.gotoHelpPage)

        # start assigning functions to map page widgets here
        self.ui.pushButtonMinimiseStats.clicked.connect(self.minimiseStats)
        self.ui.pushButtonSignOut.clicked.connect(self.signOut)


        # start assigning functions to flight data page widgets here


    def logUserIn(self):
        if not os.path.exists('credentials.csv'):
            # create credentials.csv
            with open('credentials.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "password"])
                self.ui.labelLoginError.setText("No users exist")
                file.close()


        with open('credentials.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            lineCount = 0
            # loop over the rows in the csv file

            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    if self.username == row[0] and self.password == row[1]:
                        # successful login redirect to menu page
                        self.ui.stackedWidgetMain.setCurrentIndex(1)
                        self.ui.stackedWidgetMenu.setCurrentIndex(0)
                        self.updateComPorts()

                        # show map here, instead of starting, to minimise loading time
                        self.showMap()
                    elif self.username != row[0] and self.password != row[1]:
                        self.ui.labelLoginError.setText("Wrong Username or Password")
                    elif self.username == row[0] and self.password != row[1]:
                        self.ui.labelLoginError.setText("Wrong Password")
                    elif self.username != row[0] and self.password == row[1]:
                        # if no such user exists, show error message
                        self.ui.labelLoginError.setText("Wrong Username")
                lineCount += 1


        csvFile.close()

    def signOut(self):
        self.ui.stackedWidgetMain.setCurrentIndex(0)
        self.ui.labelLoginError.setText("Signed Out")

    def signUpUser(self):
        self.ui.stackedWidgetMain.setCurrentIndex(2)

    def isValidEmail(self):
        # Regular expression pattern for Gmail addresses
        # pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com$'
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        return re.match(pattern, self.email)

    def finishSigningUp(self):
        # open credentials.csv file for writing
        with open('credentials.csv', mode='a', newline='') as credentialsFile:
            credentialsWriter = csv.writer(credentialsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # write username and password to credentials.csv file
            credentialsWriter.writerow([self.username, self.password])
        credentialsFile.close()
        if self.isValidEmail():
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

        # Initialise plane marker on map
        self.markerLayer = folium.FeatureGroup(name="Markers")
        self.m.add_child(self.markerLayer)
        self.addPlaneMarker()

        # TESTING
        # Bind the click event to the map
        marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")
        self.m.add_child(marker)
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
                radius=2000,
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.3,
                tooltip="NO FLY ZONE: " + zone["name"]
            ).add_to(self.m)

        # saves map as html
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        # htmlContent = data.getvalue().decode()

        # displays map on webEngineViewMap widget in window
        # self.ui.webEngineViewMap.setHtml(htmlContent)

        # Load the HTML template into the QWebEngineView widget
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)

        html_path = os.path.join(current_dir, "testing.html")
        print(html_path)
        with open(html_path, "r") as f:
            HTML_TEMPLATE = f.read()

        # Rest of the code remains unchanged
        self.ui.webEngineViewMap.setHtml(HTML_TEMPLATE)

    def backToLogin(self):
        self.ui.stackedWidgetMain.setCurrentIndex(0)
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

    def exitApp(self):
        # Close the serial port if it is open
        if self.serialInst.isOpen():
            self.serialInst.close()

        # Quit the application
        QCoreApplication.quit()

    def moveWindow(self, event):
        if(True):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

    def minimise(self):
        self.showMinimized()

    def setPortFromComboBox(self):
        self.selectedPort = self.ui.comboBoxCom.currentText()
        self.serialInst.port = self.selectedPort

    def setBaudFromComboBox(self):
        self.selectedBaud = int(self.ui.comboBoxBaudrate.currentText())
        self.serialInst.baudrate = self.selectedBaud

    def addPlaneMarker(self):
        if self.planeMarker is not None:
            self.removeMarker()

        self.planeMarker = folium.Marker(
            location=self.coordinate,
            popup="Plane " + str(self.coordinate),
            icon=folium.CustomIcon(icon_image="./img/plane.png", icon_size=(50, 50))
        )
        self.planeMarker.add_to(self.markerLayer)

    def removeMarker(self):
        self.markerLayer.get_root().remove_child(self.planeMarker)


    def connectSerial(self):
        print("Testing serial com ports")
        if self.ui.pushButtonConnectSerial.text() == "Connect":
            if self.selectedPort == "" or self.selectedBaud == -1:
                QMessageBox.warning(self, "Port Error", "Serial Port(COM) or Baudrate(Serial) can't be empty!")
            else:
                # Open the serial port
                self.serialInst.open()
                self.serialInst.port = self.selectedPort
                self.serialInst.baudrate = self.selectedBaud

                # Start a new thread for reading from the serial port
                self.serialThread = threading.Thread(target=self.readSerialData)
                self.serialThread.start()
        else:
            if self.serialInst.isOpen():
                self.serialInst.close()
            self.ui.pushButtonConnectSerial.setText("Connect")

    def dms_to_decimal(self):
        dms = self.latitude * self.latDir
        # 4042.6142
        degrees = int(dms / 100)        #40
        minutes = dms - (degrees * 100) #42.6142
        seconds = (minutes - int(minutes)) * 60 #36.852
        minutes = int(minutes) #42

        self.latitudeConv = round(degrees + (minutes / 60) + (seconds / 3600), 4)

        dms = self.longitude * self.lonDir
        degrees = int(dms / 100)        #40
        minutes = dms - (degrees * 100) #42.6142
        seconds = (minutes - int(minutes)) * 60 #36.852
        minutes = int(minutes) #42

        self.longitudeConv = round(degrees + (minutes / 60) + (seconds / 3600), 4)

    def readSerialData(self):
        self.ui.pushButtonConnectSerial.setText("Waiting...")
        self.ui.pushButtonConnectSerial.setEnabled(False)
        while True:
            if self.serialInst.in_waiting:
                packet = self.serialInst.readline()
                dataString = packet.decode('utf')
                print(dataString)
                # Extract and process data here
                if dataString[0:11] == '{"fix":true':
                    if(self.ui.pushButtonConnectSerial.text() == "Waiting..."):
                        self.ui.pushButtonConnectSerial.setText("Disconnect")
                        self.ui.pushButtonConnectSerial.setEnabled(True)

                    try:

                        dataDict = json.loads(dataString)

                        # Extract the required values
                        self.latitude = float(dataDict['latitude'])
                        self.longitude = float(dataDict['longitude'])
                        self.latDir = dataDict['latDir']
                        self.lonDir = dataDict['lonDir']
                        altitude = dataDict['altitude']
                        speed = dataDict['speed']
                        angle = dataDict['angle']

                        # Update the GUI
                        self.ui.labelPlaneStats.setText(f"{self.latitudeConv}\n\n{self.longitudeConv}\n\n{altitude}\n\n{speed}\n\n{angle}")

                        # decimalPlaces = 4
                        # self.latitudeConv = round(float(self.latitude[0:2]) + float(self.latitude[2:]) / 100, decimalPlaces)
                        # self.longitudeConv = round(float(self.longitude[0:2]) + float(self.longitude[2:]) / 100, decimalPlaces)


                        # convert to normal lon/lat
                        self.dms_to_decimal()
                        self.coordinate = (self.latitudeConv, self.longitudeConv)
                        # print("new coordinates received: ", self.coordinate)
                        self.addPlaneMarker()
                        self.m.save("testing.html")
                    except json.decoder.JSONDecodeError as e:
                        print("Error while parsing JSON data:", e)

    def updateComPorts(self):
        # Clear the current items in the QComboBox
        print("Refresh pressed")
        self.ui.comboBoxCom.clear()

        # Get a list of available COM ports
        comPorts = [port.device for port in serial.tools.list_ports.comports()]

        # Add the COM ports to the QComboBox
        if not comPorts:
            # If there are no available COM ports, show a dialog box
            QMessageBox.warning(self, "No COM Ports", "No COM ports found. Please check your connections and click refresh")
        else:
            # Add the COM ports to the QComboBox
            self.ui.comboBoxCom.addItems(comPorts)

    def plotFlightData(self):
        # Todo: Plot the flight data on a plot
        print("Todo: Plot the flight data on a plot")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    currentVersion = "AvASys v1.2.2"
    window = MainWindow(version=currentVersion)
    window.show()
    sys.exit(app.exec())