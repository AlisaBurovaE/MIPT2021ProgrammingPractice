def swap(function):
    def wrapper(*arguments,**flipped):
        return function(*arguments[::-1], **flipped)
    return wrapper

@swap
def div(x, y, show = False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show = True)
