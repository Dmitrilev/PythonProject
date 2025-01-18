LUOTI = 13.3
#naula = 32 * LUOTI
#leiviskä = 20 * 32 * LUOTI
leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
kg = int(((leiviskät*20*32*LUOTI)+(naulat*32*LUOTI)+(luodit*LUOTI))/1000)
gm = ((leiviskät*20*32*LUOTI)+(naulat*32*LUOTI)+(luodit*LUOTI)) % 1000
print(f"{kg} kilogrammaa ja {gm:.2f} grammaa.")