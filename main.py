from rpn.converter import toPostfix
from rpn.evaluetor import postixEval
from rpn.rpn import rpn
from rpn.checkers import check_pr

res = rpn('(34532.3^2)*3', toPostfix, postixEval, check_pr)

if res:
    print("res: ", res)
else:
    print("Error")

