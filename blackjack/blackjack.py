import hashlib
import os
import json

data_path = os.path.join(os.path.dirname(__file__), "data.json")
with open(data_path, 'r') as f:
    data = json.load(f)

def save_data(data):
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)

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

def betting():




def main():
    username, points = user_selection()
    while True:
        pass


if __name__ == "__main__":
    main()