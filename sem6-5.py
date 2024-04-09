# 5.1
max_val = int(input("Введите первое целое число: "))
repeat = int(input("Введите второе целое число: "))
s1 = []
for s in range(1, int(max_val) + 1):
    s1.append(int(s))
if len(s1 * int(repeat)) == repeat ** 2:
    s2 = s1 * int(repeat)
    print(s2)

    
# 5.2
    s3 = s2.copy()
    new_s3 = []
    for i in range(0, int(len(s3) * 0.1)):
        new_s3.append(s3[i])
    for j in range(int(len(s3) * 0.9), len(s3)):
        new_s3.append(s3[j])
    print(new_s3)
