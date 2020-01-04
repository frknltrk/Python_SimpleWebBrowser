import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.home()

    def go(self):
        url = self.address_bar.text()
        if url.find("http://") != 0:
            self.web_view.load(QUrl("http://" + url))

    def back(self):
        self.web_view.back()
    def forward(self):
        self.web_view.forward()
    def reload(self):
        self.web_view.reload()
    def home(self):
        self.web_view.load(QUrl("https://duckduckgo.com/"))

    def initUI(self):
        self.setWindowTitle("Unluturk Browser")
        self.setFixedSize(1280, 720)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.central_widget.setGeometry(QRect(10, 10, 1280, 720))
        self.vertical_layout = QVBoxLayout(self.central_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout = QHBoxLayout()

        self.back_button = QPushButton(self.central_widget)
        self.forward_button = QPushButton(self.central_widget)
        self.reload_button = QPushButton(self.central_widget)
        self.home_button = QPushButton(self.central_widget)
        self.address_bar = QLineEdit(self.central_widget)
        self.go_button = QPushButton(self.central_widget)

        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.forward_button)
        self.horizontal_layout.addWidget(self.reload_button)
        self.horizontal_layout.addWidget(self.home_button)
        self.horizontal_layout.addWidget(self.address_bar)
        self.horizontal_layout.addWidget(self.go_button)

        self.vertical_layout.addLayout(self.horizontal_layout)

        self.web_view = QWebEngineView(self.central_widget)
        self.vertical_layout.addWidget(self.web_view)

        self.address_bar.setText("www.")

        self.back_button.setIcon(QIcon("src/back.png"))
        self.back_button.setIconSize(QSize(24,24))
        self.forward_button.setIcon(QIcon("src/forward.png"))
        self.forward_button.setIconSize(QSize(24,24))
        self.home_button.setIcon(QIcon("src/home.png"))
        self.home_button.setIconSize(QSize(24,24))
        self.reload_button.setIcon(QIcon("src/refresh.png"))
        self.reload_button.setIconSize(QSize(24,24))
        self.go_button.setIcon(QIcon("src/go.png"))
        self.go_button.setIconSize(QSize(24,24))

        self.back_button.clicked.connect(self.back)
        self.forward_button.clicked.connect(self.forward)
        self.reload_button.clicked.connect(self.reload)
        self.home_button.clicked.connect(self.home)
        self.go_button.clicked.connect(self.go)

        self.address_bar.returnPressed.connect(self.go)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())