import re
import io
import sys
import csv
import json
import folium
import os.path
import threading
import serial.tools.list_ports
from ui_main import Ui_MainWindow
from emailSender import sendEmail
from urllib.request import urlopen
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox


class MainWindow(QMainWindow):

    # initialise the window with all widgets
    def __init__(self):
        # Initialising the window geometry
        super(MainWindow, self).__init__()
        self.longitudeConv = None
        self.latitudeConv = None
        self.serial_thread = None
        self.longitude = None
        self.latitude = None
        self.marker_layer = None
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
        self.zoomScale = 100
        self.selectedPort = ""
        self.selectedBaud = -1
        self.plane_marker = None


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

        # Start assigning functions to login page widgets here
        self.ui.pushButtonLogin.clicked.connect(self.logUserIn)
        self.ui.lineEditUsername.textChanged.connect(self.setUsername)
        self.ui.lineEditPassword.textChanged.connect(self.setPassword)
        self.ui.pushButtonSignup.clicked.connect(self.signUpUser)
        self.ui.pushButtonSignupNew.clicked.connect(self.finishSigningUp)
        self.ui.lineEditUsernameNew.textChanged.connect(self.setUsername)
        self.ui.lineEditPasswordNew.textChanged.connect(self.setPassword)
        self.ui.lineEditEmailNew.textChanged.connect(self.setEmail)
        self.ui.pushButtonExit.clicked.connect(self.exitApp)
        self.ui.pushButtonMinimise.clicked.connect(self.minimise)
        self.ui.frameHeader.mouseMoveEvent = self.moveWindow
        self.ui.pushButtonUpdateCOMports.clicked.connect(self.update_com_ports)
        self.ui.pushButtonConnectSerial.clicked.connect(self.connectSerial)
        self.ui.comboBoxCom.currentIndexChanged.connect(self.setPortFromComboBox)
        self.ui.comboBoxBaudrate.currentIndexChanged.connect(self.setBaudFromComboBox)
        self.ui.labelPlaneStatsDisplay.setText("Latitude:\n\nLongitude:\n\nAltitude:\n\nGroundspeed(m/s):\n\nAngle (deg):")
        self.ui.labelPlaneStats.setText("0\n\n0\n\n0\n\n0\n\n0")

        # start assigning functions to menu page widgets here
        self.ui.pushButtonFlightData.clicked.connect(self.gotoFlightDataPage)
        self.ui.pushButtonSetup.clicked.connect(self.gotoSetupPage)
        self.ui.pushButtonConfig.clicked.connect(self.gotoConfigPage)
        self.ui.pushButtonHelp.clicked.connect(self.gotoHelpPage)

        # start assigning functions to map page widgets here
        self.ui.pushButtonMinimiseStats.clicked.connect(self.minimiseStats)
        self.ui.pushButtonSignOut.clicked.connect(self.signOut)

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
                        self.update_com_ports()

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

        # Initialise plane marker on map
        self.marker_layer = folium.FeatureGroup(name="Markers")
        self.m.add_child(self.marker_layer)
        self.addPlaneMarker()

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
        self.plane_marker = folium.Marker(
            location=self.coordinate,
            popup="Plane " + str(self.coordinate),
            icon=folium.CustomIcon(icon_image="./img/plane.png", icon_size=(50, 50))
        )
        # self.m.add_child(self.plane_marker)
        self.plane_marker.add_to(self.marker_layer)

    def removeMarker(self):
        self.marker_layer.get_root().remove_child(self.plane_marker)

    def connectSerial(self):
        print("Testing serial com ports")
        if self.ui.pushButtonConnectSerial.text() == "Connect":
            if self.selectedPort == "" or self.selectedBaud == -1:
                QMessageBox.warning(self, "Port Error", "Serial Port(COM) or Baudrate(Serial) can't be empty!")
            else:
                # Open the serial port
                self.serialInst.port = self.selectedPort
                self.serialInst.baudrate = self.selectedBaud
                self.serialInst.open()

                # Start a new thread for reading from the serial port
                self.serial_thread = threading.Thread(target=self.readSerialData)
                self.serial_thread.start()

                self.ui.pushButtonConnectSerial.setText("Disconnect")
        else:

            if self.serialInst.isOpen():
                self.serialInst.close()
            self.ui.pushButtonConnectSerial.setText("Connect")

    def readSerialData(self):
        while True:
            if self.serialInst.in_waiting:
                packet = self.serialInst.readline()
                dataString = packet.decode('utf')
                print(dataString)
                if dataString[0:11] != '{"fix":true':
                    # print("Waiting to stabilise")
                    print(dataString)

                # Extract and process data here
                if dataString[0:11] == '{"fix":true':
                    data_dict = json.loads(dataString)

                    # Extract the required values
                    self.latitude = str(data_dict['latitude'])
                    self.longitude = str(data_dict['longitude'])
                    altitude = data_dict['altitude']
                    speed = data_dict['speed']
                    angle = data_dict['angle']

                    # Update the GUI
                    self.ui.labelPlaneStats.setText(f"{self.latitudeConv}\n\n{self.longitudeConv}\n\n{altitude}\n\n{speed}\n\n{angle}")

                    # Update the plane marker's position
                    # TODO: 1. Why is lat/lon conversion not working?
                    #       2. Why is the marker not updating on map (re-rendering needed?) ?
                    # convert to normal lon/lat
                    decimalPlaces = 4
                    self.latitudeConv = round(float(self.latitude[0:2]) + float(self.latitude[2:]) / 100, decimalPlaces)
                    self.longitudeConv = round(float(self.longitude[0:2]) + float(self.longitude[2:]) / 100, decimalPlaces)

                    self.coordinate = (self.latitudeConv, self.longitudeConv)
                    # print("new coordinates received: ", self.coordinate)
                    self.addPlaneMarker()
                    self.m.save("testing.html")

    def update_com_ports(self):
        # Clear the current items in the QComboBox
        print("Refresh pressed")
        self.ui.comboBoxCom.clear()

        # Get a list of available COM ports
        com_ports = [port.device for port in serial.tools.list_ports.comports()]

        # Add the COM ports to the QComboBox
        if not com_ports:
            # If there are no available COM ports, show a dialog box
            QMessageBox.warning(self, "No COM Ports", "No COM ports found. Please check your connections and click refresh")
        else:
            # Add the COM ports to the QComboBox
            self.ui.comboBoxCom.addItems(com_ports)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




















    # def connectSerial(self):
    #     print("Testing serial com ports")
    #     if self.ui.pushButtonConnectSerial.text() == "Connect":
    #         if self.selectedPort == "" or self.selectedBaud == -1:
    #             QMessageBox.warning(self, "Port Error", "Serial Port(COM) or Baudrate(Serial) can't be empty!")
    #         else:
    #             self.serialInst.open()
    #             if self.serialInst.in_waiting:
    #                 print("Serial port connected")
    #                 self.ui.pushButtonConnectSerial.setText("Disconnect")
    #                 packet = self.serialInst.readline()
    #                 dataString = packet.decode('utf')
    #                 print(dataString)
    #                 # extract data
    #                 if(dataString[0:11] == '{"fix":true'):
    #                     data_dict = json.loads(dataString)
    #
    #                     # Extract the required values
    #                     latitude = data_dict['latitude']
    #                     longitude = data_dict['longitude']
    #                     altitude = data_dict['altitude']
    #                     speed = data_dict['speed']
    #                     angle = data_dict['angle']
    #
    #                     # Print the extracted values
    #                     print("Latitude:", latitude)
    #                     print("Longitude:", longitude)
    #                     print("Altitude:", altitude)
    #                     print("Speed:", speed)
    #                     print("Angle:", angle)
    #
    #
