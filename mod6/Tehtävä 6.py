import math
def pizza(halkaisija, hinta):
    hinta / ((halkaisija/2)**2 * math.pi)
    return

suhteet = []
for i in range(1, 3):
    p = int(input(f"Anna {i}. pizzan hinta: "))
    l = int(input(f"Anna {i}. pizzan halkaisija: "))
    suhde = p/l
    suhteet.append(suhde)

if suhteet[0] < suhteet[1]:
    print("Ensimmainen pizza on kannattavampi")
else:
    print("Toinen pizza on kannattavampi")