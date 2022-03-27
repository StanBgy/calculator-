"""Model of the Calculator = handle the math"""
import re
from math import sqrt, cos, cosh, acos, sin, sinh, asin, tan, tanh, atan, pi, log, exp, log10, radians

ERROR_MSG = 'ERROR'
def calcRegex():
    calcR = re.compile(f'^\s*([-+]?)(\d+)(?:\s*([-+*\/])\s*((?:\s[-+])?\d+)\s*)+$')
    return calcR


def evaluateExpression(expression):
    """Evaluate the expresson"""
    calcR = calcRegex()
    expregex = calcR.search(expression)
    try: 
        result = str(eval(expregex.group()))
    except Exception:
        result = ERROR_MSG
    return result 

def evalExpr(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR_MSG
    return result


result = evalExpr('asin(0)')
print(result)
