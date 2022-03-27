# Controller function

from functools import partial
#from view import CalcWindow
from model import ERROR_MSG, evalExpr
import re
# Access the GUI interface 
# Handle creation of expression 
# Connect buttons and clicks 

class PyCalcCtrl:
    def __init__(self, model, view):
        # Add view and model 
        self._evaluate = model
        self._view = view
        # Add signals to view buttons when pressed 
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Clear display in case of Error"""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        """Build expression"""
        # Uses a regex to see if the expression contains an operator
        # If the expression does, do not delete the displayText
        symbol = re.compile('[-+*\/]{1}')
        if sub_exp == 'ln':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'log('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'log('
        elif sub_exp == 'Rad':
            self._view.clearDisplay()
            expression = self._view.displayText() + 'radians('
        elif sub_exp == '√':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'sqrt('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'sqrt('
        elif sub_exp == 'sin':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'sin('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'sin('
        elif sub_exp == 'cos':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'cos('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'cos('
        elif sub_exp == 'tan':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'tan('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'tan('
        elif sub_exp == 'asin':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'asin('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'asin('
        elif sub_exp == 'acos':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'acos('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'acos('
        elif sub_exp == 'atan':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'atan('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText + 'atan('
        elif sub_exp == 'log': #log10
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText() + 'log10('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'log10('
        elif sub_exp == 'e':
            expression = self._view.displayText() + 'exp('
        elif sub_exp == '1/x': 
            expression = '1/' + self._view.displayText()
        elif sub_exp == 'e^X':
            if re.search(symbol, self._view.displayText()):
                expression = self._view.displayText + 'exp('
            else:
                self._view.clearDisplay()
                expression = self._view.displayText() + 'exp('
        elif sub_exp == 'x^2':
            expression = self._view.displayText() + '*' + self._view.displayText()
        else: 
            expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)


    def _connectSignals(self):
        """Connect numbers and slots"""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'C', '='}: 
                btn.clicked.connect(partial(self._buildExpression, btnText))
        
        self._view.buttons['1/x'].clicked.connect(self._calculateResult)
        self._view.buttons['x^2'].clicked.connect(self._calculateResult)
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['Q'].clicked.connect(self._view.close)
