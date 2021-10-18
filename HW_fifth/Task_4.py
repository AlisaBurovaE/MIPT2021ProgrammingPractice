def decorator(function):
    def wrapper(array):
        count = function(array)
        if count == 0:
            print('Нет(')
        elif count > 10:
            print('Очень много')
        else:
            print(count)
    return wrapper

@decorator
def counting(array):
    count = 0
    for i in array:
        if i%2 == 0:
            count += 1
    return count

array = []
arr = input('Введите числа, напишите 000, чтобы закончить')
while arr != '000':
    array.append(int(arr))
    arr = input()

counting(array)
