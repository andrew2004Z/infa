def dell(a, x):
    return a % x == 0

def f(A, x):
    return not (not dell(x, 19) or not dell(x, 15)) or not dell(x, a)



for a in range(1, 700000):
    OK = True
    for x in range(1, 24000):
        if not f(a, x):
            OK = False
            break
    if OK:
        print(a)
        break