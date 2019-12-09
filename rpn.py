def rpn(infix, infix__postfix, postfix_evaluetor, *checkers):
    for checker in checkers:
        if not checker(infix):
            print("Invalid syntax")
            return
    postfix = infix__postfix(infix)
    res = postfix_evaluetor(postfix)
    return res