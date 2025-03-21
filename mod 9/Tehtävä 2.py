class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdytä(self, nopeuden_muutos):
            if self.tämänhetkinen_nopeus + nopeuden_muutos <= 0:
                self.tämänhetkinen_nopeus = 0
            elif self.tämänhetkinen_nopeus + nopeuden_muutos > self.huippunopeus:
                self.tämänhetkinen_nopeus = self.huippunopeus
            else:
                self.tämänhetkinen_nopeus =  self.tämänhetkinen_nopeus + nopeuden_muutos

auto1 = Auto( "ABC-123", "142")

auto1.kiihdytä(30)
auto1.kiihdytä(50)
auto1.kiihdytä(70)
print(auto1.tämänhetkinen_nopeus)
auto1.kiihdytä(-200)
print(auto1.tämänhetkinen_nopeus)


