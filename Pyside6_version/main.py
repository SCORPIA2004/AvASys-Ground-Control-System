import sys, io, folium
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
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
        # self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidgetMain.setCurrentIndex(1)


        # Start assigning functions to widgets here
        self.ui.pushButtonLogin.clicked.connect(self.logUserIn)
        self.ui.lineEditUsername.textChanged.connect(self.setUsername)
        self.ui.lineEditPassword.textChanged.connect(self.setPassword)

        mapView = QQuickWidget()
        mapView.setSource(QUrl.fromLocalFile("test_qml_box.qml"))
        self.ui.stackedWidgetMain.addWidget(mapView)


        coordinate = (39.865506432608136, 32.74609830979015)

        m = folium.Map(
            title="Bilka hill",
            zoom_start=13,
            location=coordinate
        )

        # save map data

        # folium.CircleMarker(
        #     location=coordinate,
        #     radius=5,
        #     popup="Bilkent Hill",
        #     color="red",
        #     fill=True,
        #     fill_color="red"
        # ).add_to(m)
        icon_path = "plane.png"
        icon_size = (50, 50)
        # custom_icon_html = f'<img src="{icon_path}" style="width:{icon_size[0]}px;height:{icon_size[1]}px;">'
        # folium.Marker(coordinate, icon=folium.DivIcon(html=custom_icon_html)).add_to(m)

        folium.Marker(
            location=coordinate,
            popup="Bilkent Hill",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        html_content = data.getvalue().decode()

        # mapWebView = QWebEngineView()
        self.ui.webEngineViewMap.setHtml(html_content)



    def logUserIn(self):
        if self.username == "admin" and self.password == "admin":
            self.ui.stackedWidget.setCurrentIndex(1)

    def setUsername(self, s):
        self.username = s

    def setPassword(self, s):
        self.password = s



if __name__ == '__main__':
    app = QApplication(sys.argv)
    QQuickWindow.setGraphicsApi(QSGRendererInterface.OpenGL)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())