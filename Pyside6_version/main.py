import folium
import io
import sys
import csv
import json
from urllib.request import urlopen
from PySide6.QtWidgets import *
from ui_main import Ui_MainWindow



class MainWindow(QMainWindow):

    # initialise the window with all widgets
    def __init__(self):
        # Initialising the window geometry
        super(MainWindow, self).__init__()
        self.m = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ""
        self.password = ""
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


        # start assigning functions to menu page widgets here
        self.ui.pushButtonFlightData.clicked.connect(self.gotoFlightDataPage)
        self.ui.pushButtonSetup.clicked.connect(self.gotoSetupPage)
        self.ui.pushButtonConfig.clicked.connect(self.gotoConfigPage)
        self.ui.pushButtonHelp.clicked.connect(self.gotoHelpPage)

        # start assigning functions to map page widgets here
        self.ui.pushButtonMapZoomIn.clicked.connect(self.mapZoomIn)

    def logUserIn(self):
        # open csv file
        with open('credentials.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # loop over the rows in the csv file
            for row in csv_reader:
                if self.username == row[0] and self.password == row[1]:
                    # successful login redirect to menu page
                    self.ui.stackedWidgetMain.setCurrentIndex(1)
                    # show map here, instead of starting, to minimise loading time
                    self.showMap()
                    # break
                elif self.username != row[0] and self.password != row[1]:
                    self.ui.labelLoginError.setText("Wrong Username or Password")
                    # break
                elif self.username == row[0] and self.password != row[1]:
                    self.ui.labelLoginError.setText("Wrong Password")
                    # break
                elif self.username != row[0] and self.password == row[1]:
                    # if no such user exists, show error message
                    self.ui.labelLoginError.setText("Wrong Username")
                    # break

        csv_file.close()

    def signUpUser(self):
        self.ui.stackedWidgetMain.setCurrentIndex(2)


    def finishSigningUp(self):
        # open credentials.csv file for writing
        with open('credentials.csv', mode='a', newline='') as credentials_file:
            credentials_writer = csv.writer(credentials_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # write username and password to credentials.csv file
            credentials_writer.writerow([self.username, self.password])
        credentials_file.close()
        self.ui.stackedWidgetMain.setCurrentIndex(0)

    def setUsername(self, s):
        self.username = s

    def setPassword(self, s):
        self.password = s

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
            popup="Plane",
            icon=folium.CustomIcon(icon_image="./img/plane.png", icon_size=(50, 50))
        ).add_to(self.m)

        # TESTING
        # Bind the click event to the map
        marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}")

        self.m.add_child(marker)
        # self.m.add_child(folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"))
        # END TESTING


        # saves map
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        html_content = data.getvalue().decode()

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


        urlopen("http://ipinfo.io/json")

        data = json.load(urlopen("http://ipinfo.io/json"))

        lat = data['loc'].split(',')[0]
        lon = data['loc'].split(',')[1]

        print(lat, lon)
        self.coordinate = (float(lat), float(lon))

    def mapZoomIn(self):
        print("zoom in")
        # self.ui.webEngineViewMap.page().runJavaScript("map.setZoom(15)")
        self.m = folium.Map(
            title="Flight Map",
            zoom_start=self.zoomScale - 100,
            location=self.coordinate,
            zoom_control=True,
            # tiles="Stamen Terrain"
        )




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())