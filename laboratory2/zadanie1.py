punkty = float(input("Podaj punkty: "))
if punkty > 80:
    print("Zaliczony w 0 terminie")
elif punkty <= 80 and punkty >= 50:
    print("Możesz poprawić jego wynik")
else:
    print("Musisz poprawić")
