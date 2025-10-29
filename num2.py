def calc(expr):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    priority = {"+": 1, "-": 1, "*": 2, "/": 2}

    def checker(tokens):
        values = []
        operators = []

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token == "(":
                j = i + 1
                balance = 1
                while j < len(tokens) and balance > 0:
                    if tokens[j] == "(":
                        balance += 1
                    elif tokens[j] == ")":
                        balance -= 1
                    j += 1

                sub_result = checker(tokens[i+1:j-1])
                values.append(sub_result)
                i = j
                continue

            elif token.replace(".","").isdigit():
                values.append(float(token))

            elif token in operations:
                while (operators and operators[-1] in operations and priority[operators[-1]] >= priority[token]):
                    execute_operation(values, operators, operations)
                operators.append(token)

            i += 1

        while operators:
            execute_operation(values, operators, operations)

        return values[0] if values else 0

    tokens = expr.replace("("," ( ").replace(")"," ) ").split()
    return checker(tokens)

def execute_operation(values, operators, operations):
    b = values.pop()
    a = values.pop()
    op = operators.pop()
    result = operations[op](a, b)
    values.append(result)


print(calc("1 + 2 * 3 / 4"))
print(calc("( 1 + 2 ) * 3 / 4"))
print(calc("( 1 + 1 ) * ( 1 + 1 )"))