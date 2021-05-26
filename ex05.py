s = 0
try:
    while True:
        for i in map(float, input().split()):
            s += i
        print(s)
except ValueError:
        print(s)
        