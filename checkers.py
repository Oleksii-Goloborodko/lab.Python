class Checkers:
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    def check_pr(myStr):
        stack = []
        for i in myStr:
            if i in Checkers.open_list:
                stack.append(i)
            elif i in Checkers.close_list:
                pos = Checkers.close_list.index(i)
                if ((len(stack) > 0) and
                        (Checkers.open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
