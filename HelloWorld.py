import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world!")
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create the layouts
        self.create_main_layout()
        self.create_hello_layout()
        #create central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        

    def create_main_layout(self):
        #create widgets
        self.text_box1 = QLineEdit()
        self.button = QPushButton("Submit")
        #create an instance for QVBoxLayout()
        #Add widgets to layout (self.initial_layout)
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.text_box1)
        self.initial_layout.addWidget(self.button)
        #convert layout (self.initial_layout) to widget, so it can be a 'Central widget'
        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.initial_layout)
        #Add the widget (self.initial_widget) to the stacked layout
        self.stacked_layout.addWidget(self.initial_widget)
        #button command
        self.button.clicked.connect(self.switch_layout)
        
        

    def create_hello_layout(self):
        self.helloLabel = QLabel()
        self.button.clicked.connect(self.display_text)
        self.backButton = QPushButton("Back")

        self.layout1 = QVBoxLayout()
        
        self.layout1.addWidget(self.helloLabel)
        self.layout1.addWidget(self.backButton)

        self.initial_widget1 = QWidget()
        self.initial_widget1.setLayout(self.layout1)

        self.stacked_layout.addWidget(self.initial_widget1)
        self.backButton.clicked.connect(self.back)
    

    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)

    def back(self):
        self.stacked_layout.setCurrentIndex(0)

    def display_text(self):
        name = self.text_box1.text()
        self.helloLabel.setText("Hello, {0}".format(name))
        


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
    
