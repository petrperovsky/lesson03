def div_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

print(div_func(float(input('Делимое = ')), float(input('Делитель = '))))