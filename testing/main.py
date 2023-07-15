import sys, io, folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folium Map")
        self.windowWidth, self.windowHeight = 1600, 900
        self.setMinimumSize(self.windowWidth, self.windowHeight)

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget for QMainWindow

        layout = QVBoxLayout(central_widget)  # Use the central widget for the layout

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
        # custom_icon = folium.features.CustomIcon(icon_path, icon_size=icon_path)
        custom_icon_html = f'<img src="{icon_path}" style="width:{icon_size[0]}px;height:{icon_size[1]}px;">'

        # folium.Marker(
        #     location=coordinate,
        #     popup="Bilkent Hill",
        #     icon=folium.Icon(location=coordinate, icon=folium.CustomIcon(custom_icon_html))
        # ).add_to(m)

        folium.Marker(coordinate, icon=folium.DivIcon(html=custom_icon_html)).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        html_content = data.getvalue().decode()

        mapWebView = QWebEngineView()
        mapWebView.setHtml(html_content)

        layout.addWidget(mapWebView)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
