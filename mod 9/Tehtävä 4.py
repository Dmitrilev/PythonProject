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

autot = []
voittaja = False
for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100,200) )
    autot.append(auto)
while not voittaja:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >=1000:
            voittaja = True
            break
taulu = []
for auto in autot:
    taulu.append([auto.rekisteritunnus, auto.huippunopeus, auto.tämänhetkinen_nopeus, auto.kuljettu_matka])
headers = ["rekisteritunnus", "huippunopeus", "tämänhetkinen_nopeus", "kuljettu_matka" ]
print(tabulate(taulu, headers=headers))



