def action(x, y):
    try:
        result = x + y
    except TypeError:
        print('Error: unsupported operand type(s) for +')
    else:
        print('The result is ', result)
    finally:
        print('Good job')
def second_action(x, y):
    return x / y

def third_action(x, y):
    return x * y

print(third_action(1, second_action(1, action(1, '1'))))
