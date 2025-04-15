class Auto:
    def __init__(self,rekisteritunnus, huippunopeus, tuntimäärä):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus)
        self.annettu_nopeus = 0
        self.kuljettu_matka = 0
        self.tuntimäärä = tuntimäärä


    def aseta_nopeus(self, nopeus):
        if 0 <= nopeus <= self.huippunopeus:
            self.annettu_nopeus = nopeus
        else:
            print(f"Virhe: nopeus {nopeus} km/h ei ole sallittu ({self.huippunopeus} km/h max)!")


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, tuntimäärä ):
        super().__init__(rekisteritunnus, huippunopeus, tuntimäärä)
        self.akkukapasiteetti = akkukapasiteetti
        self.kulutus_per_km = 0.2

    def ajaa(self):
        max_matka =  self.akkukapasiteetti / self.kulutus_per_km
        if self.annettu_nopeus * self.tuntimäärä >= max_matka:
            self.kuljettu_matka = max_matka
            self.akkukapasiteetti = 0

        else:
            self.kuljettu_matka += self.annettu_nopeus * self.tuntimäärä
            self.akkukapasiteetti -= self.annettu_nopeus * self.tuntimäärä * self.kulutus_per_km

    def __str__(self):
        return (f"Sahköauto:\n"
                f"Rekisteritunnus: {self.rekisteritunnus}\n"
                f"annettu_nopeus: {self.annettu_nopeus}\n"
                f"kuljettu_matka: {self.kuljettu_matka}\n"
                f"akkukapasiteetti: {self.akkukapasiteetti}\n"
                )

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, tuntimäärä):
        super().__init__(rekisteritunnus, huippunopeus, tuntimäärä)
        self. bensatankki = bensatankki
        self.kulutus_per_km = 0.08

    def ajaa(self):
        max_matka =  self.bensatankki / self.kulutus_per_km
        if self.annettu_nopeus * self.tuntimäärä >= max_matka:
            self.kuljettu_matka = max_matka
            self.bensatankki = 0
        else:
            self.kuljettu_matka += self.annettu_nopeus * self.tuntimäärä
            self.bensatankki -= self.annettu_nopeus * self.tuntimäärä * self.kulutus_per_km

    def __str__(self):
        return (f"polttomoottoriauto:\n"
                f"Rekisteritunnus: {self.rekisteritunnus}\n"
                f"annettu_nopeus: {self.annettu_nopeus}\n"
                f"kuljettu_matka: {self.kuljettu_matka}\n"
                f"bensatankki: {self.bensatankki}\n"
                )


sähköauto = Sähköauto("ABC-15", 180, 52.5, 3)
sähköauto.annettu_nopeus = int(input("Anna sähköauton nopeus( max 180 ): " ))
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3, 3)
polttomoottoriauto.annettu_nopeus = int(input("Anna polttomoottoriautom nopeus( max 165 ): " ))
sähköauto.ajaa()
polttomoottoriauto.ajaa()
print(sähköauto)
print(polttomoottoriauto)










