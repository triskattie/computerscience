import random
from gedeelde_functies import verkrijg_nummer
try:
    from InquirerPy import inquirer
except ImportError:
    inquirer = None

def rol_dobbelsteen(hoeveelheid_stenen):
    uitslag = []
    for i in range(hoeveelheid_stenen):
        uitslag.append(random.randint(1, 6))
    return uitslag

def print_scorebord(scores):
    print("\n\n\nSCOREBORD")
    for speler in scores:
        print(f"{speler}: {scores[speler]}")

def verkrijg_modus():
    if inquirer is not None:
        spel_modus = inquirer.select(
            message="Welke spelmodus wil je gebruiken?",
            choices=["Race naar 50", "Race naar 100", "5 rondes", "10 rondes"],
        ).execute()
        return spel_modus
    while True:
        try:
            gebruiker_input = int(input("""Welke spelmodus wil je gebruiken? (1-4)
1. Race naar 50
2. Race naar 100
3. 5 rondes
4. 10 rondes\n"""))
        except ValueError:
            print("Je moet een nummer invullen, probeer opnieuw.")
            continue
        if gebruiker_input > 4 or gebruiker_input < 1:
            print("Ongeldig nummer")
            continue
        return f"{'Race naar 50' if gebruiker_input == 1 else 'race naar 100' if gebruiker_input == 2 else '5 rondes' if gebruiker_input == 3 else '10 rondes'}"

def start():
    print("""Welkom bij mijn dobbelspel!\nMet hoeveel mensen ben je?""")
    while True:
        spelers = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
        if spelers <= 1:
            print("Je kan dit helaas nog niet in je eentje spelen.")
            continue
        break

    spel_modus = verkrijg_modus()
    return spelers, spel_modus

def initialiseer_spelers(n):
    scores = {}
    for i in range(n):
        while True:
            naam = input(f"Speler {i + 1}, wat is jouw naam? ")
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
        

def verkrijg_beurt_keuze():
    if inquirer is not None:
        beurt_keuze = inquirer.select(
            message="Welke actie wil je doen?",
            choices=["Dobbelen", "Challenge"],
        ).execute()
        return beurt_keuze
    while True:
        try:
            beurt_keuze = int(input("""Welke actie wil je doen? (1 of 2)
1. Dobbelen
2. Challenge"""))
        except ValueError:
            print("Ongeldig nummer")
            continue
        if beurt_keuze < 1 or beurt_keuze > 2:
            print("Ongeldig nummer")
            continue
        return f"{'dobbelen' if beurt_keuze == 1 else 'challenge'}"

def beurt(spelers, actieve_speler):
    beurt_keuze = verkrijg_beurt_keuze()
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
        if inquirer is not None:
            speler_keuze = inquirer.select(
                message="Welke speler wil je uitdagen?",
                choices=speler_keuzes,
            ).execute()
        else:
            speler_keuzes_string = ""
            index = 1
            for speler in speler_keuzes:
                speler_keuzes_string += f"{index}. {speler}\n"
                index += 1
            while True:
                try:
                    speler_keuze = int(input(f"Welke speler wil je uitdagen? (nummer)\n{speler_keuzes_string}"))
                except ValueError:
                    print("Ongeldig nummer")
                    continue
                if speler_keuze < 1 or speler_keuze > len(speler_keuzes):
                    print("Ongeldig nummer")
                    continue

            speler_keuze = speler_keuzes[speler_keuze - 1]
        input(f"{actieve_speler}, druk op enter om te dobbelen.")
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        print(f"Je hebt {dobbelsteen1} en {dobbelsteen2} gerold!")
        total1 = check(dobbelsteen1, dobbelsteen2)
        input(f"{speler_keuze}, druk op enter om te dobbelen.")
        dobbelsteen3 = random.randint(1, 6)
        dobbelsteen4 = random.randint(1, 6)
        print(f"Je hebt {dobbelsteen3} en {dobbelsteen4} gerold!")
        total2 = check(dobbelsteen3, dobbelsteen4)
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

def rondes_modus(round_amount):
    scores = initialiseer_spelers(round_amount)
    for round in round_amount:
        scores = loop(scores)

    # HIER MOET CODE KOMEN VOOR DE RONDES MODUS
    pass

def main():
    while True:
        spelers, spel_modus = start()
        if spel_modus.split()[0] == "Race":
            winnaar = race_modus(spelers, spel_modus)
            print(f"Gefeliciteerd {winnaar}, je hebt gewonnen!")
        
        if not spel_modus.split()[0].isalpha():
            round_amount = spel_modus.split()[0]
            rondes_modus(round_amount)

        

if __name__ == "__main__":
    main()