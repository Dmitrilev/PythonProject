import random
def noppa(tahko):
    return random.randint(1, tahko)

toisto = 0
n = int(input())
luku = noppa(n)
while luku != n:
    luku = noppa(n)
    toisto +=1
print(toisto)