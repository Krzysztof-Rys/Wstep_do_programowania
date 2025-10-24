
print("Równanie kwadratowe: ax^2 + bx + c = 0")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    # równanie liniowe
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Brak rozwiązań")
    else:
        x = -c / b
        print("Równanie liniowe, x =", x)
else:
    delta = b * b - 4 * a * c

    if delta < 0:
        print("Brak rozwiązań (delta < 0)")
    elif delta == 0:
        x = -b / (2 * a)
        print("Jedno rozwiązanie: x =", x)
    else:
        x1 = (-b - (delta**0.5)) / (2 * a)
        x2 = (-b + (delta**0.5)) / (2 * a)
        print("Dwa rozwiązania: x1 =", x1, ", x2 =", x2)
