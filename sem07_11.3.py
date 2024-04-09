# 1 способ

s = 'evgene_o'
sl = {'e': 3, 'v': 1, 'g': 1, 'n': 1, '_': 1, 'o': 1}
sl = {key: value for key, value in sl.items() if not value < 5}
print(sl)

# 2 способ

sl = {'e': 13, 'v': 1, 'g': 1, 'n': 1, '_': 1, 'o': 1}
for key, value in dict(sl).items():
    if value < 5:
        del sl[key]
print(sl)
