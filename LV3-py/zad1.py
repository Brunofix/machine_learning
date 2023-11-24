import pandas as pd

mtcars = pd.read_csv('mtcars.csv')
mpg_mtcars = mtcars.sort_values(by='mpg', ascending=[False])

#prvo pitanje: Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)   least mpg jer su mpg što manji to veca potrosnja
print("Auti s najvecom potrosnjom ")
print(mpg_mtcars[['car', 'mpg']].tail(5)) #zadnjih 5 u tablici



#drugo pitanje: Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print("\n  tri automobila s 8 cilindara imaju najmanju potrošnju: ")   #\n cemo staviti da nam ispisuje u novi red
print(mpg_mtcars[(mpg_mtcars.cyl == 8)][['car', 'mpg', 'cyl']].tail(3)) #zadnja tri u tablici



#trece pitanje: Kolika je srednja potrošnja automobila sa 6 cilindara?
print("\n srednja potrosnja automobila sa 6 cilindara")
print(round(mtcars[(mtcars.cyl == 6)][['mpg']].mean(), 2)) #mean funkcija izbacuje average od funkcija
#round funkcija ce nam dati zaokruzenu vrijednost nekog iznosa


#cetvrto pitanje:Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print("\n Srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs ")
print(mtcars[(mtcars.cyl == 4) & ((mtcars.wt * 1000) > 2000) & ((mtcars.wt * 1000) < 2200)][['mpg']].mean())


#peto pitanje:Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
print("\n Kolicina auta s rucnim mjenjacem je:")
print(mtcars[(mtcars.am == 1)].count()[["am"]])
print("\n Kolicina auta s automatskim mjenjacem je:")
print(mtcars[(mtcars.am ==0)].count()["am"])


# Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print("\n Kolicina automobila s automatskim mjenajcem i snagom preko 100 hp :")
print(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)].count()[['hp']])



# Kolika je masa svakog automobila u kilogramima?
print("\n Tezina svakog automobila u kilogramima:")
mtcars_kg = mtcars.copy()
mtcars_kg["wt"] = round((mtcars_kg["wt"] * 1000) * 0.45359237, 2)
print(mtcars_kg[["car", "wt"]])