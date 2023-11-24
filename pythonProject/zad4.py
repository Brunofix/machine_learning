delimiter = "X-DSPAM-Confidence: "
file=open(input("Ime datoteke:"))
avg = 0
count= 0
for line in file:
if len(line) >0 and line.startswith(delimiter):
line= line.replace(delimiter, "")
avg += float(line)
count += 1
avg/= float(count)
print("Average X-DSPAM-Confidence: %.12f" %avg)
file.close()