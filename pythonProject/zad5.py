mep = {}
file=open(input("Ime datoteke"))
for line in file:
    if len(line)>0:
        line=line.replace("\n","")
        args=line.split("")
        for i in range(0, len(args)):
            if args[i] in map:
                map[args[i]]+=1
            else:
                map[args[i]] =1

print("rijeci koje se pojavljuju samo jedanput:")
for entry in map:
    if map[entry] ==1:
        print(entry)

file.close()