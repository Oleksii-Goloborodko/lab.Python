from .helpers import Operators

class Converter:
    def toPostfix(infix: str) -> list:
        """ Converts infix to postfix notation.

        :param (str) infix: Infix string
        :returns (list): List of postfix notation
        """
        stack = []
        postfix = []
        i = 0
        for c in infix:
            try:
                c = infix[i]
            except IndexError:
                continue
            if Operators.isOperand(c):
                buf = Operators.isNumberOperand(c, infix, i)
                postfix.append(buf)
                i += len(buf)
            else:
                i += 1
                if Operators.isLeftParenthesis(c):
                    stack.append(c)
                elif Operators.isRightParenthesis(c):
                    operator = stack.pop()
                    while not Operators.isLeftParenthesis(operator):
                        postfix.append(operator)
                        operator = stack.pop()
                else:
                    while (not (stack == [])) and Operators.hasLessOrEqualPriority(c, stack[-1]):
                        postfix.append(stack.pop())
                    stack.append(c)

        while (not (stack == [])):
            postfix.append(stack.pop())
        return postfix
