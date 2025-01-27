import random
luku = random.randint(1,10)
arvo = int(input("Arvaa luku väliltä 1..10: "))
while arvo != luku:
    if arvo < luku:
        print("Liian pieni arvaus")
    elif arvo > luku:
        print("Liian suuri arvaus")
    arvo = int(input("Arvaa luku väliltä 1..10: "))
print("Oikein")