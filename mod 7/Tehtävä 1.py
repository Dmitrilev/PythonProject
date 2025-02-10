vuodenaika = ("Talvi", "Kevät", "Kesä", "Syksy")
numero = int(input("Anna kuukauden numero: "))
if 1<numero<=3:
    print(vuodenaika[0])
elif 3<numero<=6:
    print(vuodenaika[1])
elif 6<numero<=9:
    print(vuodenaika[2])
elif 9<numero<=12:
    print(vuodenaika[3])