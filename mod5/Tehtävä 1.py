import random
määrä = int(input("Anna arpakuutioiden lukumäärä: "))
tulokset = []
summa = 0
for i in range(määrä):
    luku = random.randint(1,6)
    tulokset.append(luku)
for n in tulokset:
    summa +=n
print(summa)

