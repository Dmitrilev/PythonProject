import random
def noppa():
    return random.randint(1,6)

toisto = 0
luku = noppa()
while luku != 6:
    luku = noppa()
    toisto +=1
print(toisto)