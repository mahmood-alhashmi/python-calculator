# token initialisation 
numbers = []
ops = []
expression_token = []

import sympy


def Current_token(expression):
    # token initialisation 
    numbers = []
    ops = []
    i=0

    while i < len(expression):
        if expression[i].isdigit():
            j=i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            expression_token.append(expression[i:j])
            i = j
        elif expression[i] in "+-/*^()":
            expression_token.append(expression[i])
            i += 1
        elif expression[i].isalpha():
            j=i
            while j < len(expression) and (expression[j].isalpha()):
                j += 1
            expression_token.append(expression[i:j])
            i = j
        else:
            i += 1
    return expression_token

expression = "3 + 5 * sin(0.5)"
print(Current_token(expression))
