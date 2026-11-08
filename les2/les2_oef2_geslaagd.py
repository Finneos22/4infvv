behaaldepunten= float(input ("Hoeveel punten behaalde je"))
maximum= float(input("Wat was de maximaal te behalen score"))
if behaaldepunten/maximum*100 >= 50:
    score= "Proficiat,geslaagd"
if behaaldepunten/maximum*100 < 50:
    score= "Jammer, niet geslaagd"
print(score)