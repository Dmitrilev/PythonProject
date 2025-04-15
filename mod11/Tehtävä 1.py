class Kirja:
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

class Tiedot_kirja(Kirja):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi, kirjoittaja, sivumäärä)
        print(vars(self))


class Lehti:
    def __init__(self, nimi, päätoimittaja):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja

class Tiedot_lehti(Lehti):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi, päätoimittaja)
        print(vars(self))

kirja = Tiedot_kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Tiedot_lehti("Aku Ankka", "Aki Hyyppä")

