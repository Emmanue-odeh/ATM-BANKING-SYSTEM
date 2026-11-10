import json
import secrets
import hashlib
import hmac
from datetime import datetime

FILE = "accounts.json"

def load_accounts():
    try:
        with open(FILE, "r") as file:
            accounts = json.load(file)
            if not isinstance(accounts, dict):
                raise SystemExit("Invalid accounts.json format.")
            return accounts
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        raise SystemExit("Your accounts.json file is damaged.")


def save_accounts(accounts):
    try:
        with open(FILE, "w") as file:
            json.dump(accounts, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save account information.")
        return False


def hash_pin(pin, salt=None):
    salt = salt or secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac(
        "sha256", pin.encode(), salt.encode(), 100000
    ).hex()
    return salt, hashed


def verify_pin(account, pin):
    salt, hashed = hash_pin(pin, account["pin_salt"])
    return hmac.compare_digest(hashed, account["pin_hash"])


def generate_account_number(accounts):
    while True:
        number = str(secrets.randbelow(9000000000) + 1000000000)
        if number not in accounts:
            return number


def register(accounts):
    print("\n===== CREATE ACCOUNT =====")
    name = input("Full name: ").strip()
    phone = input("Phone number: ").strip()

    if not name or not phone or not phone.isdigit():
        print("Enter a valid name and phone number.")
        return

    pin = input("Create a 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    if pin != input("Confirm PIN: "):
        print("PINs do not match.")
        return

    number = generate_account_number(accounts)
    salt, hashed = hash_pin(pin)

    accounts[number] = {
        "name": name,
        "phone": phone,
        "pin_salt": salt,
        "pin_hash": hashed,
        "balance": 0,
        "transactions": []
    }

    if save_accounts(accounts):
        print(f"Account created! Welcome, {name}.")
        print(f"Your account number is: {number}")


def login(accounts):
    number = input("Account number: ").strip()

    if number not in accounts:
        print("Account does not exist.")
        return None

    account = accounts[number]
    pin = input("PIN: ")

    if "pin" in account and account["pin"] == pin:
        salt, hashed = hash_pin(pin)
        account["pin_salt"] = salt
        account["pin_hash"] = hashed
        del account["pin"]
        save_accounts(accounts)
        return number

    if "pin_salt" in account and verify_pin(account, pin):
        print(f"Welcome back, {account['name']}!")
        return number

    print("Incorrect PIN.")
    return None


def money_transaction(accounts, number, action):
    account = accounts[number]

    try:
        amount = int(input("Enter amount: ₦"))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Enter a valid positive whole-number amount.")
        return

    if action == "Withdrawal" and amount > account["balance"]:
        print("Insufficient balance.")
        return

    if action == "Deposit":
        account["balance"] += amount
    else:
        account["balance"] -= amount

    account["transactions"].append({
        "type": action,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    if save_accounts(accounts):
        print(f"Successful! Balance: ₦{account['balance']:,}")


def account_menu(accounts, number):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance")
        print("4. Transaction History\n5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            money_transaction(accounts, number, "Deposit")
        elif choice == "2":
            money_transaction(accounts, number, "Withdrawal")
        elif choice == "3":
            print(f"Balance: ₦{accounts[number]['balance']:,}")
        elif choice == "4":
            history = accounts[number]["transactions"]
            if not history:
                print("No transactions yet.")
            for item in history:
                print(item)
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid option.")


def main():
    accounts = load_accounts()

    while True:
        print("\n===== SMART ATM =====")
        print("1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register(accounts)
        elif choice == "2":
            number = login(accounts)
            if number:
                account_menu(accounts, number)
        elif choice == "3":
            print("Thank you for using Smart ATM!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nATM closed.")
