getal1 = int(input("geef getal 1: "))
getal2 = int(input("geef getal 2: "))
bewerking = input ("Welke bewerking wil je uitvoeren? (+,-,/,*,m):")

if bewerking == "+":  #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan; != : Niet gelijk aan
    print(f"De som van {getal1} en {getal2} = {getal1+getal2}.")

if bewerking == "-":
    print (f"{getal1} - {getal2} = {getal1-getal2}.")

if bewerking == "/":
    print (f"{getal1} / {getal2} = {getal1/getal2}.")

if bewerking == "*":
    print (f"{getal1} . {getal2} = {getal1*getal2}.")

if bewerking == "m":
    print (f"{getal1} ** {getal2} = {getal1**getal2}.")