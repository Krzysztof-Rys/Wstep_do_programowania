stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)
ilosc_stopnii = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie


print("ilość stopnie:",ilosc_stopnii)
print("index majora:",Major_index)
print("czy występuje pułkownik:",Pułkownik_wstepowanie)
