import random
from tabulate import tabulate
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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            if auto.kuljettu_matka <1000:
                auto.kiihdytä(random.randint(-10, 15))
                auto.kulje(1)
            if auto.kuljettu_matka > 1000:
                return

    def tulosta_tilanne(self):
        taulu = []
        for auto in self.autot:
            taulu.append([auto.rekisteritunnus, auto.huippunopeus, auto.tämänhetkinen_nopeus, auto.kuljettu_matka])
        headers = ["rekisteritunnus", "huippunopeus", "tämänhetkinen_nopeus", "kuljettu_matka"]
        print(tabulate(taulu, headers=headers))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= 1000:
                return True
                break


autot = []
voittaja = False
for i in range(10):
    auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot )
tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti +=1
    if tunti % 10 == 0:
        print(f"Välitulokset {tunti}:n tunnin kuluttua ")
        kilpailu.tulosta_tilanne()
print(f"\nKilpailun lopputulokset {tunti}:n kuluttua")
kilpailu.autot.sort(key = lambda auto: auto.kuljettu_matka, reverse = True)
kilpailu.tulosta_tilanne()



