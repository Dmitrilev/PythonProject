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
    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä

auto1 = Auto( "ABC-123", "142")

#Esimerkki
auto1.tämänhetkinen_nopeus = 60
auto1.kuljettu_matka = 2000
auto1.kulje(1.5)
print(f"{int(auto1.kuljettu_matka)} km")