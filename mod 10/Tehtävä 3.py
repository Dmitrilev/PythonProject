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
                print(f"Täällä hetkellä hissi numero {hissin_numero} on {self.nykyinen_kerros}:ssä kerroksessa")
            print("Olet paikalla")
            while self.nykyinen_kerros != self.alin_kerros:
                self.kerros_alas()
                print(f"Täällä hetkellä hissi numero hissin_numero on {self.nykyinen_kerros}:ssä kerroksessa")

class Talo:
    def __init__(self,alin_kerros,ylin_kerros, hiisienlukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissienlista = []
        for i in range(hiisienlukumäärä):
            hissi = Hissi(alin_kerros,ylin_kerros)
            self.hissienlista.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissienlista[hissin_numero-1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("Talossa on palo! Kaikki hissit menevät alas")
        for hissi in self.hissienlista:
            while hissi.nykyinen_kerros != alin_kerros:
                hissi.kerros_alas()

alin_kerros = int(input("Syötä alin kerros: "))
ylin_kerros = int(input("Syötä ylin kerros: "))
hiisienlukumäärä = int(input("Anna hiisien lukumäärä: "))
talo = Talo(alin_kerros, ylin_kerros, hiisienlukumäärä)
hissin_numero = int(input("Anna hissin numero: "))
kohdekerros = int(input("Mihin kerrokseen haluat: "))
talo.aja_hissiä(hissin_numero,kohdekerros)
talo.palohälytys()
