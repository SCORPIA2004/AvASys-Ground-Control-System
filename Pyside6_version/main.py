import folium
import io
import sys
import csv

from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        # Initialising the window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ""
        self.password = ""

        # Start window at Login page
        self.ui.stackedWidgetMain.setCurrentIndex(0)

        # Start assigning functions to login page widgets here
        self.ui.pushButtonLogin.clicked.connect(self.logUserIn)
        self.ui.lineEditUsername.textChanged.connect(self.setUsername)
        self.ui.lineEditPassword.textChanged.connect(self.setPassword)


        # start assigning functions to menu page widgets here
        self.showMap()
        self.ui.pushButtonFlightData.clicked.connect(self.gotoFlightDataPage)
        self.ui.pushButtonSetup.clicked.connect(self.gotoSetupPage)
        self.ui.pushButtonConfig.clicked.connect(self.gotoConfigPage)
        self.ui.pushButtonHelp.clicked.connect(self.gotoHelpPage)



        # mapView = QQuickWidget()
        # self.ui.webEngineViewMap.setSource(QUrl.fromLocalFile("test_qml_box.qml"))
        # self.ui.stackedWidgetMenu.addWidget(self.ui.webEngineViewMap)

    def logUserIn(self):
        # open csv file and check if username and password are correct
        with open('credentials.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                # print(f"\trow[0] BUT {self.username}")
                if self.username == row[0] and self.password == row[1]:
                    self.ui.stackedWidgetMain.setCurrentIndex(1)
                line_count += 1

        # if self.username == "admin" and self.password == "admin":
        #     self.ui.stackedWidgetMain.setCurrentIndex(1)
        print("No such user")



    def setUsername(self, s):
        self.username = s

    def setPassword(self, s):
        self.password = s

    def showMap(self):
        coordinate = (39.865506432608136, 32.74609830979015)
        m = folium.Map(
            title="Bilka hill",
            zoom_start=13,
            location=coordinate
        )
        # TODO: change the icon of marker to a plane
        icon_path = "plane.png"
        icon_size = (50, 50)
        # custom_icon_html = f'<img src="{icon_path}" style="width:{icon_size[0]}px;height:{icon_size[1]}px;">'
        # folium.Marker(coordinate, icon=folium.DivIcon(html=custom_icon_html)).add_to(m)
        # End of TODO1
        folium.Marker(
            location=coordinate,
            popup="Bilkent Hill",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)


        data = io.BytesIO()
        m.save(data, close_file=False)
        html_content = data.getvalue().decode()

        self.ui.webEngineViewMap.setHtml(html_content)

    def gotoFlightDataPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(1)

    def gotoSetupPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(2)

    def gotoConfigPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(3)

    def gotoHelpPage(self):
        self.ui.stackedWidgetMenu.setCurrentIndex(4)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())