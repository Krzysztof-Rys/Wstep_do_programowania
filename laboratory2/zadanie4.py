gol = int(input("podaj liczbe goli:"))
bonus = 0
punkty = gol * 10
# A
# if gol > 5 and gol < 10:
#     bouns =+5
# elif gol > 10:
#     bonus =+10
# punkty+=bonus
# print(punkty)

# B

if gol > 5:
    bonus=bonus+5
if gol > 10:
    bonus=10+bonus
punkty+=bonus
print(punkty)