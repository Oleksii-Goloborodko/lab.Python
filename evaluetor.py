class Actions:
    def add(a: float, b: float) -> float:
        """ Add two numbers

        :param (int) a: First number
        :param (int) b: Second number
        :returns (int): Sum of two numbers
        """
        return a + b

    def minus(a: float, b: float) -> float:
        """ Substruct b from a
        :param (int) a: left operand.
        :param (int) b: right operand
        :returns (int): Result of substruction
        """
        return b - a

    def multiply(a: float, b: float) -> float:
        """ Multiply two numbers

        :param (int) a: First number
        :param (int) b: Second number
        :returns (int): Multiply of two numbers
        """
        return a * b

    def division(a: float, b: float) -> float:
        """ Diviaion two numbers

        :param (int) a: First number
        :param (int) b: Second number
        :returns (int): Division of two numbers
        """
        return b / a

    def power(a: float, b: float) -> float:
        """ Add two numbers

            :param (int) a: First number
            :param (int) b: Second number
            :returns (int): Division of two numbers
         """
        return pow(b, a)

    def dot_float(a: int, b: int) -> float:
        return float(str(b) + "." + str(a))

    operators = {
        '.': dot_float,
        '+': add,
        '-': minus,
        '*': multiply,
        '/': division,
        '^': power
    }

    def postixEval(stack: list) -> float:
        """ Evaluate postfix notation

        :param (list) stack: Stack with postfix notation
        :returns (float): Result of evaluation
        """
        res = list()
        for symbol in stack:
            if symbol.isdigit():
                res.append(int(symbol))
            elif not (res == []):
                temp = Actions.operators.get(symbol)(res.pop(), res.pop())
                res.append(temp)
        return res.pop()



