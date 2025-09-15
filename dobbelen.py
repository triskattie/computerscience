import random
from gedeelde_functies import verkrijg_nummer

def rol_dobbelsteen(hoeveelheid_stenen):
    uitslag = []
    for i in range(hoeveelheid_stenen):
        uitslag.append(random.randint(1, 6))
    return uitslag

def print_scorebord(scores):
    print("SCOREBORD")
    for speler in scores:
        print(f"{scores[speler].key()}: {scores[speler]}")


def main():
    while True:
        print("""Welkom bij mijn dobbelspel!\nMet hoeveel mensen ben je? """)
        spelers = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
        print("Hoeveel rondes wil je doen?")
        rondes = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
        scores = {}
        for speler in spelers:
            scores[f"Speler {speler + 1}": 0]
        print_scorebord()

        

if __name__ == "__main__":
    main()