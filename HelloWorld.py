import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

print('Hello')
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world!")
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create the layouts
        self.create_main_layout()
        self.create_hello_layout()
        self.create_convert()
        #create central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        

    def create_main_layout(self):
        #create widgets
        self.text_box1 = QLineEdit()
        self.button = QPushButton("Submit")
        self.label123 = QLabel("Enter your name into the box right away")
        #create an instance for QVBoxLayout()
        #Add widgets to layout (self.initial_layout)
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.text_box1)
        self.initial_layout.addWidget(self.button)
        self.initial_layout.addWidget(self.label123)
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
        self.convertButton = QPushButton("Convert")

        self.layout1 = QVBoxLayout()
        
        self.layout1.addWidget(self.helloLabel)
        self.layout1.addWidget(self.backButton)
        self.layout1.addWidget(self.convertButton)

        self.initial_widget1 = QWidget()
        self.initial_widget1.setLayout(self.layout1)

        self.stacked_layout.addWidget(self.initial_widget1)
        self.backButton.clicked.connect(self.back)
        self.convertButton.clicked.connect(self.convert)

    def create_convert(self):
        
        self.note = QLabel("Name converting coming soon!")

        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.note)

        self.widget3 = QWidget()
        self.widget3.setLayout(self.layout3)

        self.stacked_layout.addWidget(self.widget3)
        
    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)

    def back(self):
        self.stacked_layout.setCurrentIndex(0)

    def display_text(self):
        name = self.text_box1.text()
        self.helloLabel.setText("Hello, {0}".format(name))
    def convert(self):
        self.stacked_layout.setCurrentIndex(2)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
    
