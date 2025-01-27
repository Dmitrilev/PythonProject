luku = input("Anna luku: ")
arvo = int(luku)
min_arvo = arvo
max_arvo = arvo
while luku !="":
    arvo = int(luku)
    if arvo <= min_arvo:
        min_arvo = arvo
    elif arvo >= max_arvo:
        max_arvo = arvo
    luku = input("Anna luku: ")
print(f"min. arvo = {min_arvo}\nmax. arvo = {max_arvo} ")
