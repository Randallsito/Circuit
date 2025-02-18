import json

def llegirArixiuJson():
    with open("entradesCircuit.json","r",encoding="utf-8") as fitxer:
        return (json.load(fitxer)["localitats"])

def escriureArxiuJson(localitat):
    with open("entradesCircuit.json","w",encoding="utf-8") as fitxer:
        json.dump({"localitats":localitat}, fitxer, indent=4)

def mostrarLocalitats():
    localitats = llegirArixiuJson()
    print(f"{'nom':<25} ¨{'preu (€)':<10} {'Entrades disponibles'}")
    print("-" * 70)
    for localitat in localitats:
        print(f"{localitat['nom']:<25} {localitat['preu']:<10} {localitat['entrades_disponibles']} ")


def reservarLocalitat():
    pass
    
def menu():
    while True:
        print("-" * 70)
        print("Benvingut al circuit de Barcelona Cataluña")
        print("-" * 70)
        print("1. Mostrar localitats a resevar")
        print("2. Reservar entrada")
        print("3. Sortir")

        opcio = int(input("Introdueix una opccio valida: "))
        
        match opcio: 
            case 1:
                mostrarLocalitats()
            case 2:
                reservarLocalitat()
            case 3: 
                break
            case _:
                print("Opcio no valida")


menu()