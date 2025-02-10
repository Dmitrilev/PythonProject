lentoasemat = {}

while True:
    print("Toiminnot:")
    print(" 1. Syöttää uuden lentoaseman")
    print(" 2. Hakea jo syötetyn lentoaseman tiedot")
    print(" 3. Lopettaa")
    toiminto = input("Valitse toiminto(1,2 tai 3): ")
    if toiminto == "1":
        icao_koodi = input("Anna lentoaseman ICAO - koodin: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
    elif toiminto == "2":
        avain = input("Anna lentoaseman ICAO - koodin:  ")
        print(f"Lentoaseman nimi: {lentoasemat[avain]}")
    elif toiminto == "3":
        print("Ohjelma kesketty")
        break
