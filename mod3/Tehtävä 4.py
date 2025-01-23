vuosi = int(input("Mikä on vuosiluku: "))
if vuosi % 100 != 0 and vuosi % 4 == 0 or vuosi % 100 == 0 and vuosi % 4 == 0 and vuosi % 400 == 0:
    print("Se on karkausvuosi.")
else:
    print("Se ei ole karkausvuosi")

