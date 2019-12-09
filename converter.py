from .helpers import isNumberOperand
from .helpers import isOperand
from .helpers import isLeftParenthesis
from .helpers import isRightParenthesis
from .helpers import hasLessOrEqualPriority

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
      if isOperand(c):
          buf = isNumberOperand(c, infix, i)
          postfix.append(buf)
          i += len(buf)
      else:
          i += 1
          if isLeftParenthesis(c):
              stack.append(c)
          elif isRightParenthesis(c):
              operator = stack.pop()
              while not isLeftParenthesis(operator):
                  postfix.append(operator)
                  operator = stack.pop()              
          else:
              while (not (stack == [])) and hasLessOrEqualPriority(c,stack[-1]):
                  postfix.append(stack.pop())
              stack.append(c)
      """i += 1"""

  while (not (stack == [])):
      postfix.append(stack.pop())
  return postfix