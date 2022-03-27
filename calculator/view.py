# view/main file
"""Main Window-Style App"""

import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

from controller import PyCalcCtrl
from model import evalExpr

class CalcWindow(QMainWindow):
    """Main Window"""
    def __init__(self, parents=None):
        super().__init__(parents)
        # Main window's properties 
        self.setWindowTitle('Calculator')
        self.setFixedSize(512, 512)
        # Set widget layout 
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # Display Widget
        self.display = QLineEdit()
        # set some propoerties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add display to general layout
        self.generalLayout.addWidget(self.display)

    def setDisplayText(self, text):
        """Set display text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

    def _createButtons(self):
        # Create grid layout
        self.buttons = {} # Each buttons will be associated with a position
        grid = QGridLayout()
        # buttons position
        buttons = {'pi': (0,0),
                'Rad': (0,1),
                '√': (0,2),
                'C': (0, 3),
                '(': (0, 4),
                ')': (0, 5),
                '/': (0, 6),
                'sin': (1,0),
                'cos': (1,1),
                'tan': (1,2),
                '7': (1, 3),
                '8': (1, 4),
                '9': (1, 5),
                '*': (1, 6),
                'asin': (2,0),
                'acos': (2,1),
                'atan': (2,2),
                '4': (2, 3),
                '5': (2, 4),
                '6': (2, 5),
                '-': (2, 6),
                'e^X': (3, 0),
                'x^2': (3, 1),
                '1/x': (3, 2),
                '1': (3, 3),
                '2': (3, 4),
                '3': (3, 5),
                '+': (3, 6),
                'ln': (4,0),
                'log' : (4,1),
                'e': (4,2),
                '0': (4, 3),
                '.': (4, 4),
                '=': (4, 5),
                'Q': (4, 6),
                }
        for btnNbm, pos in buttons.items(): 
            self.buttons[btnNbm] = QPushButton(btnNbm)
            self.buttons[btnNbm].setFixedSize(40, 40)
            grid.addWidget(self.buttons[btnNbm], pos[0], pos[1])

        self.equal = QPushButton('=')
        self.equal.setFixedSize(80, 80)
       # grid.addWidget(self.equal, 4, 2, 1, 2)
        self.generalLayout.addLayout(grid)


def main(): 
    pycalc = QApplication(sys.argv)
    view = CalcWindow()
    view.show()
    # Create instance of the Controller 
    model = evalExpr
    PyCalcCtrl(model=model, view=view)
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
