imie = input('Podaj imie: ')
print("witaj ", imie)
wiek = int(input('Podaj wiek: '))
print("Twój wiek to:", wiek)
nazwisko = input('Podaj nazwisko: ')
print("twoje inicjały to:", imie[0], nazwisko[0])

lancuch = input('Podaj łancuch: ')
for i in range(0,5):
    print(lancuch)

lancuch = input('podaj łańcuch')
lancuch2 = input('podaj łańcuch2')

lancuch3 = lancuch + lancuch2
print(lancuch3)
lancuch3_3=lancuch[0:len(lancuch)//2] + lancuch2[len(lancuch2)//2:]

print(lancuch3_3)