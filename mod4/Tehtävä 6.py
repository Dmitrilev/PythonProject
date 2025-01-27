import random
N = int(input("Syötä pisteiden määrä: "))
toisto = 0
n = 0
while toisto != N:
    toisto += 1
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if (a**2 + b**2) < 1:
        n += 1
print(f"Piin likiarvo on {4*n/N}")



