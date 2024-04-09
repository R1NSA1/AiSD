# 1
l1 = ['1', '123', '123', '12', '1', '123']
print([len(i) for i in l1])

# 2
l1 = ['1', '123', '123', '12', '1', '123']
print([len(i) for i in l1 if len(i) > 2])

# 3
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([l2[i] * (i + 1) for i in range(len(l2))])

# 4
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i for i in l2 if i > 0])

# 5
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([l2[i] if l2[i] > 0 else i + 1 for i in range(len(l2))])

# 6
s = 'abcdef'
print({s[i]: i + 1 for i in range(len(s))})

# 7
l1 = ['1', '123', '20', '12', '1', '123']
d1 = {'123': 10, '2': 20, '3': 30, '4': 40}
print(len(list([i for i in l1 if i in d1])))

# 8
s = 'evgene_o'
print({s[i]: s.count(s[i]) for i in range(len(s))})

# 9
d = {'e': 3, 'v': 1, 'g': 1, 'n': 1, '_': 1, 'o': 1}
print(len([i for i in d if i.islower()]))

# 10
d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sorted({i * d4[i] for i in d4}))

# 11
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
print({i: d6[i] for i in d6 if i not in d5})

# 12
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
print({i: j for i, j in d6.items() if i not in d5 and d5})

# 13
s = 'SIX,SEVEN,EIGHT,NINE,TEN'
a = []
s1 = s.split(',')
for i in range(len(s1) + 1):
    print(i)
    if i % 2 == 0:
        a.append(s1[i])
print(', '.join(a))

# 14
def calc_op(s, oper_d):
    for oper in oper_d:
        if oper in s:
            return oper_d[oper](*list(map(int, s.split(oper))))
        
        
print(calc_op('2 a 10', {'a': lambda x,y: x+y }))
print(calc_op('2 s 10', {'s': lambda x,y: x** y }))

# 15
s = [1, 2, 3, 4, 5]
print(a)

# 16
s = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]
s1 = []
for i in range(len(s)):
    print(''.join(s[i]))
    s1.append(''.join(s[i]))
print(', '.join(s1))

# 17
d = {'a': 1, 'b': 3, 'c': 4, 'd': 3}
d1 = {v: k for k, v in d.items() if list(d.values()).count(v) == 1}
print(d1)

# 18
d =  {(2,4): 'a', (1,1,1): 'b', (2,3): 'c'}
d1 = {sum(k) / len(k): v for k, v in d.items()}
print(d1)
