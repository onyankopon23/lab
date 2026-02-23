"""Simple calculator module"""


def calc(first_number, second_number, operation):
    """ "Calculator operations"""

    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("division by 0")
        return first_number / second_number

    raise ValueError("unknown operation")
