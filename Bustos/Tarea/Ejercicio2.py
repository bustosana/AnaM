
#---------------------

ternas = []
for a in range (1,501):
    for b in range (1,501):
        for c in range (1,501):
            if a**2 + b**2 == c**2:
                ternas.append((a,b,c))
print("cantidad de ternas",len(ternas))

for t in ternas:
    print(t)
