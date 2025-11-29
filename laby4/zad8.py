stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)
ilosc_stopnii = 0
for i in stopnie:
    ilosc_stopnii+=1

print(stopnie.index("Major"))



for i in stopnie:
    if "Major" in stopnie:
        Pułkownik_wstepowanie = True
    else:
        Pułkownik_wstepowanie = False
print(Pułkownik_wstepowanie)