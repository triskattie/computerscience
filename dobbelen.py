"""
Naam: PRIVACY
Programma: dobbelen.py
Werking: Dit programma is een spelletje waarbij de gebruiker een doel in kan stellen en vervolgens met 2 of meer spelers
gaat dobbelen tot het doel bereikt is. Het programma werkt het best met de module "InquirerPy" die te installeren is met
"pip install inquirerpy" in een terminal. Het kan ook gespeeld worden zonder.
"""

import random
from gedeelde_functies import verkrijg_nummer
try:
    from InquirerPy import inquirer
except ImportError:
    inquirer = None

# Print het scorebord met inputs scores en ronde nummer
def print_scorebord(scores, r : int = None):
    print(f"\n\n\nSCOREBORD {f'RONDE {r + 1}' if r else ''}")
    # Sorteert de scores door eerst een tuple te maken met (key, value) en dan telkens de value te pakken. Reversed
    # zodat het aflopend is.
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    for speler in sorted_scores:
        print(f"{speler}: {sorted_scores[speler]}")

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

def intro():
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
            if naam == "" or naam in scores: #Als de gebruiker niets invult of een naam die al bestaat, invult
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
2. Challenge
"""))
        except ValueError:
            print("Ongeldig nummer")
            continue
        if beurt_keuze < 1 or beurt_keuze > 2:
            print("Ongeldig nummer")
            continue
        print(beurt_keuze)
        return f"{'Dobbelen' if beurt_keuze == 1 else 'Challenge'}"

def beurt(scores, actieve_speler):
    beurt_keuze = verkrijg_beurt_keuze()
    if beurt_keuze == "Dobbelen":
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        print(f"Je hebt {dobbelsteen1} en {dobbelsteen2} gerold!")
        final_result = check(dobbelsteen1, dobbelsteen2)
        scores[actieve_speler] += final_result
        return scores
    else: #Wanneer challenge is gekozen
        alle_spelers = list(scores.keys())
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
                break

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
            scores[actieve_speler] += total
        elif total2 > total1:
            print(f"{speler_keuze} heeft {total} verdiend!")
            scores[speler_keuze] += total
        else:
            print(f"{actieve_speler} heeft {total1} verdiend en {speler_keuze} heeft {total2} verdiend!")
            scores[actieve_speler] += total1
            scores[speler_keuze] += total2
        return scores




def loop(scores, r):
    print_scorebord(scores, r)
    for speler in scores:
        print(f"\n\n{speler} is nu aan de beurt!")
        scores = beurt(scores, speler)
    return scores

def race_modus(scores, spel_modus):
    doel = int(spel_modus.split()[-1])
    scores = initialiseer_spelers(scores)
    r = 0
    while max(scores.values()) < doel:
        scores = loop(scores, r)
        r += 1
    winnaar = max(scores, key=scores.get)
    return winnaar, scores

def rondes_modus(round_amount, scores):
    scores = initialiseer_spelers(scores)
    for r in range(round_amount):
        scores = loop(scores, r)
    winnaar = max(scores, key=scores.get)
    return winnaar, scores

def main():
    while True:
        scores, spel_modus = intro()
        if spel_modus.split()[0] == "Race":
            winnaar, scores = race_modus(scores, spel_modus)
            print(f"Gefeliciteerd {winnaar}, je hebt gewonnen!")
            print_scorebord(scores)
        
        if not spel_modus.split()[0].isalpha():
            round_amount = int(spel_modus.split()[0])
            winnaar, scores = rondes_modus(round_amount, scores)
            print(f"Gefeliciteerd {winnaar}, je hebt gewonnen!")
            print_scorebord(scores)

        

if __name__ == "__main__":
    main()