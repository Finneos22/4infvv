tijd= float(input("Hoeveel seconden telde je tussen de bliksem en de donder?"))
afstand= round(tijd*0.3,3)
print(f"Je bent {afstand} km van het onweer verwijderd")

if afstand >= 3:
    print("Je bent veilig.")
if afstand < 3:
    print("Ga plat op de grond liggen!")