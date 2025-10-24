import random

droga = random.randint(4, 300)

srednie_spalanie = float(input("Podaj średnie spalanie (w litrach na 100km):"))

cena_paliwa = float(input("Podaj aktualną cene paliwa za litr:"))

zuzycie_paliwa = (droga * srednie_spalanie)/100
koszt = round(zuzycie_paliwa * cena_paliwa,2)
print(f'Przewidywane zużycie paliwa: {zuzycie_paliwa} ')
print(f'Szacowany koszt podróży:{koszt} zł')

