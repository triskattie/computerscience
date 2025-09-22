import hashlib
import os
import json
from json import JSONDecodeError

from gedeelde_functies import verkrijg_nummer
import random

def save_data(data):
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)

data_path = os.path.join(os.path.dirname(__file__), "data.json")
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

def beurt_keuze(player_cards, points):
    if len(player_cards) == 2:
        double = True
        if player_cards[0] == player_cards[1]:
            split_possible = True

def print_cards(computer_cards, player_cards):
    computer_cards_string = "  ".join(computer_cards)
    print("COMPUTER CARDS")
    print(computer_cards_string)
    player_cards_string = "  ".join(player_cards)
    print("PLAYER CARDS")
    print(player_cards_string)
    while True:


def game_round(username, points):
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Joker"]
    computer_cards = []
    for i in range(2):
        computer_cards.append(random.choice(cards))
    player_cards = []
    for i in range(2):
        player_cards.append(random.choice(cards))

    print_cards(computer_cards, player_cards)
    return


def main():
    username, points = user_selection()
    while True:
        bet = betting(points)
        points = game_round(username, points)
        save_data(points)


if __name__ == "__main__":
    main()