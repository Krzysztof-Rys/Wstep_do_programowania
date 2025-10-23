x = [1+2, 1 + 4.5, 3 / 2, 4 / 2, 3 // 2, -3 // 2, 11 % 2, 2 ** 10, 8 ** (1/3)]
i=0
for j in range(len(x)):
    print(f'{i+1}. = {x[i]} {type(x[i])}')
    i+=1


# print(int(3.0))
# print(float(3))
# print(float("3"))
# print(str(12.4))
# print(bool(0))
