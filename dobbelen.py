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
        scores[f"Speler {n + 1}"] = 0

def check():
    pass

def beurt():
    beurt_keuze = inquirer.select(
        message="Welke actie wil je doen?",
        choices=["Dobbelen", "Challenge"],
    ).execute()
    if beurt_keuze == "Dobbelen":
        # HIER VERDER

def loop(spelers):
    pass

def race_modus(spelers, spel_modus):
    doel = spel_modus.strip()[-1]
    scores = initialiseer_spelers(spelers)
    while max(scores) < doel:
        scores = loop(scores)
    winnaar = max(scores)
    return winnaar

def rondes_modus():
    # HIER MOET CODE KOMEN VOOR DE RONDES MODUS
    pass

def main():
    while True:
        spelers, spel_modus = start()
        if spel_modus.split()[0] == "Race":
            race_modus(spelers, spel_modus)
        
        if not spel_modus.split()[0].isalpha():
            rondes_modus()

        

if __name__ == "__main__":
    main()