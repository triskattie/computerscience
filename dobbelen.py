import random
from gedeelde_functies import verkrijg_nummer
from InquirerPy import inquirer

def rol_dobbelsteen(hoeveelheid_stenen):
    uitslag = []
    for i in range(hoeveelheid_stenen):
        uitslag.append(random.randint(1, 6))
    return uitslag

def print_scorebord(scores):
    print("\n\n\nSCOREBORD")
    for speler in scores:
        print(f"{speler}: {scores[speler]}")

def start():
    print("""Welkom bij mijn dobbelspel!\nMet hoeveel mensen ben je? """)
    while True:
        spelers = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
        if spelers <= 1:
            print("Je kan dit helaas nog niet in je eentje spelen.")
            continue
        break

    spel_modus = inquirer.select(
        message="Welke spelmodus wil je gebruiken?",
        choices=["Race naar 50", "Race naar 100", "5 rondes", "10 rondes"],
    ).execute()
    return spelers, spel_modus

def initialiseer_spelers(n):
    scores = {}
    for i in range(n):
        while True:
            naam = input(f"Speler {i + 1}, wat is jouw naam?")
            if naam == "" or naam in scores:
                print("Naam niet beschikbaar, probeer opnieuw.")
                continue
            break
        scores[naam] = 0
    return scores

def check(dice1, dice2, result: int = 0):
    result += dice1 + dice2
    if dice1 == 6 and dice2 == 6:
        input("Je hebt geluk! Je mag nog een keer dobbelen, druk op enter om te dobbelen.")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Je hebt {dice1} en {dice2} gerold!")
        result = check(dice1, dice2, result)
    return result
        



def beurt(spelers, actieve_speler):
    beurt_keuze = inquirer.select(
        message="Welke actie wil je doen?",
        choices=["Dobbelen", "Challenge"],
    ).execute()
    if beurt_keuze == "Dobbelen":
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        print(f"Je hebt {dobbelsteen1} en {dobbelsteen2} gerold!")
        final_result = check(dobbelsteen1, dobbelsteen2)
        spelers[actieve_speler] += final_result
        return spelers
    else: #Wanneer challenge is gekozen
        alle_spelers = list(spelers.keys())
        alle_spelers.remove(actieve_speler)
        speler_keuzes = alle_spelers
        speler_keuze = inquirer.select(
            message="Welke speler wil je uitdagen?",
            choices=speler_keuzes,
        ).execute()
        input(f"{actieve_speler}, druk op enter om te dobbelen.")
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        total1 = check(dobbelsteen1, dobbelsteen2)
        print(f"Je hebt {dobbelsteen1} en {dobbelsteen2} gerold!")
        input(f"{speler_keuze}, druk op enter om te dobbelen.")
        dobbelsteen3 = random.randint(1, 6)
        dobbelsteen4 = random.randint(1, 6)
        total2 = check(dobbelsteen3, dobbelsteen4)
        print(f"Je hebt {dobbelsteen3} en {dobbelsteen4} gerold!")
        total = total1 + total2
        if total1 > total2:
            print(f"{actieve_speler} heeft {total} verdiend!")
            spelers[actieve_speler] += total
        elif total2 > total1:
            print(f"{speler_keuze} heeft {total} verdiend!")
            spelers[speler_keuze] += total
        else:
            print(f"{actieve_speler} heeft {total1} verdiend en {speler_keuze} heeft {total2} verdiend!")
            spelers[actieve_speler] += total1
            spelers[speler_keuze] += total2
        return spelers




def loop(spelers):
    for speler in spelers:
        print(f"\n\n{speler} is nu aan de beurt!")
        spelers = beurt(spelers, speler)
    print_scorebord(scores=spelers)
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