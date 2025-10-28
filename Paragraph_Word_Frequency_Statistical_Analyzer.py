l = []
d = {}
oot = 0
taf = 0
mtf = 0


while True:
    x = input("Enter a line (or 'END' to finish): ").split()
    if (x.count("END") == 1) or (x.count("end") == 1):
        break
    else:
        for i in x:
            i = i.lower()
            if i[-1] == "," or i[-1] == ".":
                i = i[:-1]
            l.append(i)
            

for j in l:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

for key, value in d.items():
    if d[key] == 1 or d[key] == 2:
        oot += 1
    elif d[key] == 3 or d[key] == 4:
        taf += 1
    elif d[key] > 4:
        mtf += 1 

print("1. Number of words that appear once or twice: %d" %oot)
print("2. Number of words that appear three and four times: %d" %taf)
print("3. Number of words that appear more than four times: %d" %mtf)
    
