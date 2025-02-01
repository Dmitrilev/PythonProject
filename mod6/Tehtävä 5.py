def parillinen(lukuja):
    for i in lukuja:
        if i % 2 != 0:
            lukuja.remove(i)
            n = lukuja
    return n

luku = input("Anna luku: ")
luvut = []
while luku != "":
    luvut.append(luku)
    luku = input("Anna luku: ")
luvut_sorted = list(map(int, luvut))
print("Alkuperäinen lista: ", *luvut,"\n" + "Karsittu lista: ", *parillinen(luvut_sorted))