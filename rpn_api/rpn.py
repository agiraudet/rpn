def rpn_eval(expr):
    stack = []
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    tokens = expr.split()
    for tok in tokens:
        if tok in ops:
            if len(stack) < 2:
                raise ValueError(
                    "Invalid RPN expression: insufficient operands.")
            y = stack.pop()
            x = stack.pop()
            try:
                res = ops([tok](x, y))
                stack.append(res)
            except ZeroDivisionError:
                raise ValueError("Invalid RPN expression: division by zero")
        else:
            try:
                stack.append(float(tok))
            except ValueError:
                raise ValueError(
                    f"Invalid RPN expression: invalid operand: {tok}")
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many operands")
    return stack[0]
