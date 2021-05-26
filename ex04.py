def my_func(x, y):
    '''Возведение в отрицательноую степень'''
    step = 1
    for i in range(abs(y)):
        step *= x
    return 1 / step

print(my_func(float(input('Действительное положительное число: ')), int(input('Целое отрицательное число: '))))