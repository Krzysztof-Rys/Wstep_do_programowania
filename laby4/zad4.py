zdanie = input("Podaj zdanie: ")

zdanie_male = zdanie.lower()

litery = [litera for litera in zdanie_male if 'a' <= litera <= 'z']

litery.sort()
print(litery)

alfabet = set("abcdefghijklmnopqrstuvwxyz")

litery_w_zdaniu = set(litera for litera in zdanie_male if 'a' <= litera <= 'z')

brakujace_litery = sorted(list(alfabet - litery_w_zdaniu))

print("Brakujące litery:", "".join(brakujace_litery))
