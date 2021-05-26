def my_func(a, b, c):
    '''Сумма наибольших двух из трех заданных аргументов'''
    my_list = [a, b, c]
    my_min = min(my_list)
    my_list.remove(my_min)
    return sum(my_list)

print(my_func(int(input('Число 1: ')), int(input('Число 2: ')), int(input('Число 3: '))))
