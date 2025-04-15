class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1

    def kerros_alas(self):
        self.nykyinen_kerros -=1


    def siirry_kerrokseen(self,kohdekerros):
        if kohdekerros == self.nykyinen_kerros:
            print("Olet jo tässä kerroksessä")
        elif kohdekerros >self.ylin_kerros:
            print(f"Talossa on vain {self.ylin_kerros}")
        else:
            while self.nykyinen_kerros != kohdekerros:
                self.kerros_ylös()
                print(f"Täällä hetkellä hissi on {self.nykyinen_kerros}:ssä kerroksessa")
                print("Olet paikalla")
            while self.nykyinen_kerros != self.alin_kerros:
                self.kerros_alas()
                print(f"Täällä hetkellä hissi on {self.nykyinen_kerros}:ssä kerroksessa")

hissi = Hissi(int(input("Syötä alin kerros: ")), int(input("Syötä ylin kerros: ")))
hissi.siirry_kerrokseen(int(input("Mihin kerrokseen haluat?")))

