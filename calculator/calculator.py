import sys 
# https://realpython.com/python-pyqt-gui-calculator/

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout, QPushButton

app = QApplication(sys.argv)


# Create an instance of the application
window = QWidget()
window.setWindowTitle('PyQt5 App')
layout = QGridLayout()
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
layout.addWidget(QPushButton('Button (2, 1) + 2 col span'), 2, 1, 1, 2)
window.setLayout(layout)
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World</1>', parent=window)
helloMsg.move(60, 15)

window.show()

# Run the App event loop
sys.exit(app.exec_())
