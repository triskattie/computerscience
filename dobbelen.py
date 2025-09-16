import random
from gedeelde_functies import verkrijg_nummer
from InquirerPy import inquirer

def rol_dobbelsteen(hoeveelheid_stenen):
    uitslag = []
    for i in range(hoeveelheid_stenen):
        uitslag.append(random.randint(1, 6))
    return uitslag

def print_scorebord(scores):
    print("SCOREBORD")
    for speler in scores:
        print(f"{speler}: {scores[speler]}")

def start():
    print("""Welkom bij mijn dobbelspel!\nMet hoeveel mensen ben je? """)
    spelers = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
    spel_modus = inquirer.select(
        message="Welke spelmodus wil je gebruiken?",
        choices=["Race naar 50", "Race naar 100", "5 rondes", "10 rondes"],
    ).execute()
    return spelers, spel_modus

def initialiseer_spelers(n):
    scores = {}
    for i in range(n):
        scores[f"Speler {i + 1}"] = 0
    return scores

def check(dice1, dice2, result: int = 0):
    result += dice1 + dice2
    if dice1 == 6 and dice2 == 6:
        a = input("Je hebt geluk! Je mag nog een keer dobbelen, druk op enter om te dobbelen.")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Je hebt {dice1} en {dice2} gerold!")
        result = check(dice1, dice2, result)
    return result
        



def beurt():
    beurt_keuze = inquirer.select(
        message="Welke actie wil je doen?",
        choices=["Dobbelen", "Challenge"],
    ).execute()
    if beurt_keuze == "Dobbelen":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Je hebt {dice1} en {dice2} gerold!")
        final_result = check(dice1, dice2)
        return final_result

def loop(spelers):
    for speler in spelers:
        print(f"{speler} is nu aan de beurt!")
        spelers[speler] += beurt()
    return spelers

def race_modus(spelers, spel_modus):
    doel = int(spel_modus.split()[-1])
    scores = initialiseer_spelers(spelers)
    while max(scores.values()) < doel:
        scores = loop(scores)
    winnaar = max(scores, key=scores.get)
    return winnaar

def rondes_modus():
    # HIER MOET CODE KOMEN VOOR DE RONDES MODUS
    pass

def main():
    while True:
        spelers, spel_modus = start()
        if spel_modus.split()[0] == "Race":
            winnaar = race_modus(spelers, spel_modus)
            print(f"Gefeliciteerd {winnaar}, je hebt gewonnen!")
        
        if not spel_modus.split()[0].isalpha():
            rondes_modus()

        

if __name__ == "__main__":
    main()