try:
ocjena=float(input("Unesite ocjenu izmedju 0.0 i 1.0"))
except:
print("Pogresan unos, unesite ocjenu izmedju 0.0 i 1.0")
exit()

if ocjena >= 0.9:
kategorija = "A"
elif ocjena >= 0.8:
kategorija = "B"
elif ocjena >= 0.7:
kategorija ="C"
elif ocjena >= 0.6:
kategorija= "D"
else :
kategorija= "F"

print(f"Kategorija ocjene je: {kategorija}")