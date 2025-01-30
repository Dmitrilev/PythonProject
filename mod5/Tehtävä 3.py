luku = int(input("Anna luku: "))
alkuluku = True
if luku == 1:
    print("Se ei ole alkuluku")
else:
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break
    if alkuluku:
        print("Se on alkuluku")
    else:
        print("Se ei ole alkuluku")
