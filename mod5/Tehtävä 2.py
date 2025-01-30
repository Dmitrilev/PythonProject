merkki = input("Anna luku: ")
lista = []
while merkki != "":
    lista.append(merkki)
    merkki = input("Anna luku: ")
lista_sorted = sorted(lista, key=int)
print(*lista_sorted[-1:-6:-1])