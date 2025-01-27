käyttäjätunnus = input("Käyttäjätunnus: ")
salasana = input("salasana: ")
k = 1
while käyttäjätunnus !="python" and salasana !="rules":
    if k == 5:
        print("Pääsy evätty")
        break
    käyttäjätunnus = input("Käyttäjätunnus: ")
    salasana = input("salasana: ")
    k += 1
else:
    print("Tervetuloa")