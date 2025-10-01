import hashlib
import os
import json
from json import JSONDecodeError
import time

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gedeelde_functies import verkrijg_nummer
import random

def save_data(data):
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)

data_path = os.path.join(os.path.dirname(__file__), "data.json")
if not os.path.exists(data_path):
    data = {
        "Logins": {},
        "Balances": {}
    }
    save_data(data)
else:
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except JSONDecodeError:
        data = {
            "Logins": {},
            "Balances": {}
        }
        save_data(data)



def hash_passwd(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()

def user_selection():
    while True:
        username = input("Please enter your username: ")
        if username not in data['Logins']:
            print("This username does not exist yet, do you want to continue? (y/n)")
            while True:
                yn = input("")
                if yn.lower() in ["y", "yes"]:
                    break
                elif yn.lower() in ["n", "no"]:
                    break
                else:
                    print("Please enter y or n")
            if yn.lower() in ["n", "no"]:
                break

            # Continuing with account creation
            password = input("Please create a password: ")
            password_hash = hash_passwd(password)
            data["Logins"][username] = password_hash
            data["Balances"][username] = 1000
            save_data(data)
            print("Your account has been created")
            return username, 1000
        else:
            attempt = 0
            if attempt > 2:
                print("Too many attempts.")
                exit(1)
            while True:
                password = input("Please enter your password: ")
                if hash_passwd(password) != data["Logins"][username]:
                    attempt += 1
                    print("Incorrect password, try again.")
                else:
                    points = data["Balances"][username]
                    return username, points

def betting(limit):
    while True:
        print("How many points would you like to bet? ")
        amount = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=True)
        if amount > limit:
            print(f"You don't have enough points! You have {limit} points.")
            continue
        return amount

def beurt_keuze(player_cards, points, bet):
    if len(player_cards) == 2:
        double = True
    else:
        double = False
    choice_string = "\n1. Hit\n2. Stand"
    amount_of_possibilities = 2
    if double:
        amount_of_possibilities += 1
        choice_string += "\n3. Double"
    while True:
        player_choice = input(f"Which option would you like to choose?{choice_string} ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            print("Please enter a number.")
            continue
        if player_choice > amount_of_possibilities:
            print("Invalid input, please try again.")
            continue
        break
    return "hit" if player_choice == 1 else "stand" if player_choice == 2 else "double"

def get_value(cards):
    value = 0
    for card in cards:
        try:
            value += int(card)
        except ValueError:
            if card == "J":
                value += 10
            elif card == "Q":
                value += 10
            elif card == "K":
                value += 10
            elif card == "A":
                value += 11
    if value > 21 and "A" in cards:
        value -= 10
    return value



def print_cards(computer_cards, player_cards, first: bool = True):
    if first:
        computer_cards_string = "  ".join(computer_cards[0])
        computer_cards_string += "  CLOSED"
        computer_cards_string += f"  ({get_value(computer_cards[0])})"
    else:
        computer_cards_string = "  ".join(computer_cards)
        computer_cards_string += f"  ({get_value(computer_cards)})"

    print("COMPUTER CARDS")
    print(computer_cards_string)
    player_cards_string = "  ".join(player_cards)
    player_cards_string += f"  ({get_value(player_cards)})"
    print("PLAYER CARDS")
    print(player_cards_string)


def game_round(username, points, bet):
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Joker"]
    computer_cards = []
    for i in range(2):
        new_card = random.choice(cards)
        if new_card == "Joker":
            new_card = "10"
        computer_cards.append(new_card)
    player_cards = []
    for i in range(2):
        new_card = random.choice(cards)
        if new_card == "Joker":
            print("Your new card is a joker, you may now pick a number between 1 and 10.")
            while True:
                number = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
                if number > 10:
                    print("Smaller than 10.")
                    continue
                break
            new_card = str(number)
        player_cards.append(new_card)


    while True:
        print_cards(computer_cards, player_cards)
        skip = False
        if get_value(computer_cards) == 21 or get_value(player_cards) == 21:
            skip = True
            keuze = ""
        if not skip:
            keuze = beurt_keuze(player_cards, points, bet)
        if keuze == "hit":
            new_card = random.choice(cards)
            if new_card == "Joker":
                print("Your new card is a joker, you may now pick a number between 1 and 10.")
                while True:
                    number = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)
                    if number > 10:
                        print("Smaller than 10.")
                        continue
                    break
                new_card = str(number)

            player_cards.append(new_card)
            if get_value(player_cards) < 21:
                continue
        elif keuze == "stand":
            done = True
        elif keuze == "double":
            bet *= 2
            player_cards.append(random.choice(cards))
            done = True
        if not skip:
            while get_value(computer_cards) < 17:
                new_card = random.choice(cards)
                if new_card == "Joker":
                    if get_value(computer_cards) <= 11:
                        new_card = "10"
                    else:
                        new_card = 21 - get_value(computer_cards)
                computer_cards.append(new_card)
                print_cards(computer_cards, player_cards, first = False)
        print_cards(computer_cards, player_cards, first = False)
        if get_value(player_cards) == 21:
            return points + bet * 1.5
        if get_value(computer_cards) > 21:
            return points + bet
        if get_value(player_cards) > 21 or get_value(computer_cards) == 21 or get_value(player_cards) < get_value(computer_cards):
            return points - bet
        if get_value(player_cards) > get_value(computer_cards):
            return points + bet
        if get_value(player_cards) == get_value(computer_cards):
            return points


def main():
    username, points = user_selection()
    while True:
        print(f"You have {points} points.")
        bet = betting(points)
        points = game_round(username, points, bet)
        data["Balances"][username] = points
        save_data(data)


if __name__ == "__main__":
    main()