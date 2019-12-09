from rpn.checkers import Checkers

class Rpn:
    def rpn(infix, infix__postfix, postfix_evaluetor, *checkers):
        for Checkers.checker in checkers:
            if not Checkers.checker(infix):
                print("Invalid syntax")
                return
        postfix = infix__postfix(infix)
        res = postfix_evaluetor(postfix)
        return res
