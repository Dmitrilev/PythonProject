nimi = input("Syötä nimi: ")
nimet = set()

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
    nimi = input("Syötä nimi: ")
for n in nimet:
    print(n)
