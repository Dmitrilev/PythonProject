import random
for i in range(3):
    s = random.randint(0, 9)
    print(s, end = '')
    if i == 3:
        print()
for r in range(4):
    d = random.randint(1, 6)
    print(d, end = '')