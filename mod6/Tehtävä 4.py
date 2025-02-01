def summa(lukuja):
    n = sum(lukuja)
    return n

N = input("Anna luku: ")
luvut = []
while N != "":
    luvut.append(N)
    N = input("Anna luku: ")
luvut_sorted = list(map(int, luvut))
print("Summa:", summa(luvut_sorted))
