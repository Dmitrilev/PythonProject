import math
def pizza(halkaisija, hinta):
    return hinta / ((halkaisija/2)**2 * math.pi)

suhteet = []
for i in range(1, 3):
    p = float(input(f"Anna {i}. pizzan hinta: "))
    l = float(input(f"Anna {i}. pizzan halkaisija: "))
    suhteet.append(pizza(l,p))

if suhteet[0] < suhteet[1]:
    print("Ensimmainen pizza on kannattavampi")
else:
    print("Toinen pizza on kannattavampi")