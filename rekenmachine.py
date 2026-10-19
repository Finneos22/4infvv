getal1 = int(input("geef getal 1: "))
getal2 = int(input("geef getal 2: "))
bewerking = input ("Welke bewerking wil je uitvoeren? (+,-,/,*):")

#We berekenen de som
som = getal1 + getal2

print("De som is "+str(som) )
#print("De som van" + "en" + getal2+ "is" +som + ".") Dit is een andere manier van tekst.
print(f"De som van {getal1} en {getal2} is {som}")