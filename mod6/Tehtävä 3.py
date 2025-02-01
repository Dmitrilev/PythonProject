def muunnos(galonna):
    return galonna * 3.785

määrä = float(input("Anna galonnamäärä: "))
while määrä >0:
    print(muunnos(määrä), "litraa")
    määrä = float(input())