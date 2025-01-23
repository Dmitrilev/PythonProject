s = input("Sinun biologinen sukupuoli: ")
hem = float(input("Sinun hemoglobiiniarvo: "))
if s == "nainen":
    if hem < 117:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif 117<hem<175:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")
if s == "mies":
    if hem < 134:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif 134<hem<195:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")