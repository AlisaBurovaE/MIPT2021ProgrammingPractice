def action(x, y):
    try:
        result = x + y
    except TypeError:
        print('Error: unsupported operand type(s) for +')
    else:
        print('The result is ', result)
    finally:
        print('Good job')
print(action(1, 3), action(1, '3'))
