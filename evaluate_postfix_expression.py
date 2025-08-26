def evaluate_postfix(expr):
    if not expr:
        return "Error: Empty expression"

    stack = []
    operators = '+-*/'

    for char in expr:
        if char.isdigit():  # if it's a number
            stack.append(int(char))
        elif char in operators:  # if it's an operator
            if len(stack) < 2:
                return "Error: Not enough operands"

            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                if b == 0:
                    return "Error: Division by zero"
                stack.append(a / b)
        else:
            return f"Error: Invalid character '{char}'"

    if len(stack) != 1:
        return "Error: Extra operands left after processing"

    return stack[0]

# ---------- Examples ----------
expressions = ["42+3*", "", "5", "4+", "40/", "42a+", "42"]
for st in expressions:
    result = evaluate_postfix(st)
    print(f"Expression: {st}, Result: {result}")
