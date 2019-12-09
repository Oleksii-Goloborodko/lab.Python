from rpn.converter import Converter
from rpn.evaluetor import Actions
from rpn.rpn import Rpn
from rpn.checkers import Checkers

def toFixed(numObj, digits = 0):
    return f"{numObj:.{digits}f}"


res = Rpn.rpn('(65+21)*3', Converter.toPostfix, Actions.postixEval, Checkers.check_pr)

if res:
    print("res: ", toFixed(res, 4))
else:
    print("Error")

