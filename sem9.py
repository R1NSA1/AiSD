#4.13
l1 = ['1', '123', '123', '12', '1', '123']
print([len(i) for i in l1])

#4.14
l1 = ['1', '123', '123', '12', '1', '123']
print(len([len(i) for i in l1 if len(i) > 2]))

#4.15
d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 8:30}
print(sorted({k * v for k, v in d4.items()}))

#4.16
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
print({k: v for k, v in d6.items() if k not in d5})  

#4.17
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i * l2[i] for i in range(len(l2))])

#4.18 (1)
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i for i in l2 if i > -1])

#4.18 (2)
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i if i > -1 else _ for i in l2])

#4.19
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i if i > -1 else l2[i] for i in l2])

#5.1
def mn(a, b):
    return a * b


c = int(input("Введите первый множитель: "))
d = int(input("Введите второй множитель: "))
pr = mn(c, d)
print("Произведение:", pr)

#5.4 (1)
def op(*n):
    r = 1
    for x in n:
        r *= x
    return r


op(1, 2, 3)

#5.4 (2)
def f(x, *y, **m):
    res = x
    for t in y: res *= t
    z = 1
    for k, x in m.items():
        z = z*x
    return res


f(2, 4, 4)

#5.5 (1)
def op(n, n1, n2):
    if n == '+':
        return n1 + n2
    elif n == '-':
        return n1 - n2
    elif n == '*':
        return n1 * n2
    elif n == '/':
        return n1 / n2


op('+', 2, 2)

#5.5 (2) 
def op(n1, n2, n):
    n11 = str(n2)
    rez = eval(str(n1) + n + n11)
    return rez


op(2, 2, '+')
