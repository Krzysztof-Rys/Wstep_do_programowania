lista_zakupow = {
    'karmel':25.34,
    'bułki':34.21,
    'awokado':12.32,
    'jaszczurka':543.23,
    'kahon':234.99

}

for i in lista_zakupow.keys():
    print(i)
print(f'suma pieniążków:{sum(lista_zakupow.values())}')
