# Smart ATM System

## Project Description

Smart ATM is a simple terminal-based banking application built with Python. It allows users to create bank accounts, log in securely, deposit money, withdraw money, check their account balance, and view their transaction history.

The project demonstrates how Python functions, conditional statements, loops, dictionaries, and JSON file handling can be used to build a practical application.

## How the Program Works

When the program starts, it loads existing customer account information from the `accounts.json` file. This allows previously registered customers to access their accounts even after the program has been closed.

The application displays a main menu with three options:

1. Create Account
2. Login
3. Exit

### 1. Account Creation

When a new customer selects Create Account, the program requests their full name, phone number, and a four-digit PIN.

It validates the information to ensure that the required details are provided and that the PIN contains exactly four digits.

The program then generates a unique account number and securely hashes the customer's PIN before saving the account information in `accounts.json`.

### 2. Customer Login

Customers can log in using their account number and PIN.

The program checks whether the account number exists and verifies the entered PIN against the securely stored PIN hash.

If the details are correct, the customer gains access to their account menu.

### 3. Depositing Money

Customers can deposit money into their accounts by entering an amount.

The program checks that the amount is a valid positive whole number. If the deposit is successful, the account balance is updated and the transaction is recorded.

### 4. Withdrawing Money

Customers can withdraw money from their accounts.

The program validates the withdrawal amount and checks that the customer has enough money in their account.

Withdrawals that exceed the available balance are rejected to prevent overdrafts.

### 5. Checking Account Balance

Customers can view their current account balance at any time after logging in.

### 6. Transaction History

The program records successful deposits and withdrawals, including the transaction type, amount, and date and time.

Customers can view their transaction history through their account menu.

### 7. Saving Account Information

The application uses JSON file handling to store customer information, account balances, and transaction history.

Whenever an account is created or a financial transaction is completed, the updated information is saved to `accounts.json`.

This allows account information to remain available when the application is restarted.

## Technologies and Python Concepts Used

- **Python:** Main programming language.
- **JSON:** Stores customer accounts and transaction information.
- **Functions:** Organize the application into smaller reusable sections.
- **Dictionaries:** Store customer account details.
- **Lists:** Store transaction history.
- **Loops:** Keep the application and customer menus running.
- **Conditional Statements:** Handle menu selections and validate operations.
- **Exception Handling:** Handle errors such as missing files and invalid inputs.
- **Hashing:** Protects customers' PINs instead of storing them as readable text.

## How to Run the Project

1. Make sure Python is installed on your computer.
2. Download or clone the project.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python3 main.py / & "$HOME\.local\bin\python3.14.exe" gui.py
```

## Project Structure

```text
smart-atm/
│
├── main.py
├── accounts.json
└── README.md
```

## Project Goal

The goal of this project is to strengthen my understanding of Python programming fundamentals by building a practical banking application that demonstrates account management, data storage, input validation, and transaction processing.

This project is a learning simulation and is not intended for real banking transactions.
