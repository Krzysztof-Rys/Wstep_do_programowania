a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

if a == 0:
    if b == 0:
        print("Nieskończenie wiele rozwiązań")
    else:
        print("Brak rozwiązań")
else:
    x = -b / a
    print("x =", x)