
import tkinter as tk
import main


# ==========================================
# SMART ATM - PREMIUM DARK BANKING SYSTEM
# ==========================================

root = tk.Tk()

root.title("Smart ATM | Digital Banking")
root.geometry("1250x780")
root.minsize(1100, 700)
root.configure(bg="#090B16")


# ==========================================
# COLOUR PALETTE
# ==========================================

BG = "#090B16"
SIDEBAR = "#0D1020"
CARD = "#111528"
CARD_LIGHT = "#171C35"

BLUE = "#315BFF"
PURPLE = "#7047FF"
CYAN = "#26C6F4"

WHITE = "#FFFFFF"
TEXT = "#E8ECFF"
MUTED = "#858DAA"
BORDER = "#252B46"
SUCCESS = "#32D583"
ERROR = "#FF6B81"


# ==========================================
# SCREEN CONTAINERS
# ==========================================

login_frame = tk.Frame(root, bg=BG)
register_frame = tk.Frame(root, bg=BG)
dashboard_frame = tk.Frame(root, bg=BG)

dashboard_frame.grid_rowconfigure(0, weight=1)
dashboard_frame.grid_columnconfigure(1, weight=1)


# ==========================================
# SCREEN NAVIGATION FUNCTIONS
# ==========================================

def show_login():

    register_frame.pack_forget()
    dashboard_frame.pack_forget()

    login_frame.pack(fill="both", expand=True)


def show_register():

    login_frame.pack_forget()
    dashboard_frame.pack_forget()

    register_frame.pack(fill="both", expand=True)


# ==========================================
# LOGIN SCREEN
# ==========================================

login_frame.grid_rowconfigure(0, weight=1)
login_frame.grid_columnconfigure(0, weight=1)

login_card = tk.Frame(
    login_frame,
    bg=CARD,
    padx=45,
    pady=40,
    highlightthickness=1,
    highlightbackground=BORDER
)

login_card.grid(row=0, column=0)


login_brand = tk.Label(
    login_card,
    text="◆  SMART ATM",
    font=("Arial", 23, "bold"),
    bg=CARD,
    fg=WHITE
)

login_brand.pack(pady=(5, 12))


login_subtitle = tk.Label(
    login_card,
    text="Your finances. Your control.",
    font=("Arial", 10),
    bg=CARD,
    fg=MUTED
)

login_subtitle.pack(pady=(0, 35))


login_heading = tk.Label(
    login_card,
    text="Welcome Back",
    font=("Arial", 21, "bold"),
    bg=CARD,
    fg=WHITE
)

login_heading.pack(anchor="w")


login_description = tk.Label(
    login_card,
    text="Sign in to access your banking dashboard.",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

login_description.pack(anchor="w", pady=(7, 25))


# Account number
account_label = tk.Label(
    login_card,
    text="ACCOUNT NUMBER",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

account_label.pack(anchor="w", pady=(0, 8))


account_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=BLUE
)

account_entry.pack(fill="x", ipady=12, pady=(0, 20))


# PIN
pin_label = tk.Label(
    login_card,
    text="4-DIGIT PIN",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

pin_label.pack(anchor="w", pady=(0, 8))


pin_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    show="*",
    highlightthickness=1,
    highlightbackground=BORDER,
    highlightcolor=BLUE
)

pin_entry.pack(fill="x", ipady=12, pady=(0, 20))


login_message = tk.Label(
    login_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=ERROR
)

login_message.pack(anchor="w", pady=(0, 12))


# ==========================================
# REGISTRATION SCREEN
# ==========================================

register_frame.grid_rowconfigure(0, weight=1)
register_frame.grid_columnconfigure(0, weight=1)

register_card = tk.Frame(
    register_frame,
    bg=CARD,
    padx=45,
    pady=25,
    highlightthickness=1,
    highlightbackground=BORDER
)

register_card.grid(row=0, column=0)


register_brand = tk.Label(
    register_card,
    text="◆  SMART ATM",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=WHITE
)

register_brand.pack(pady=(5, 10))


register_heading = tk.Label(
    register_card,
    text="Create Your Account",
    font=("Arial", 21, "bold"),
    bg=CARD,
    fg=WHITE
)

register_heading.pack(pady=(10, 5))


register_description = tk.Label(
    register_card,
    text="Join Smart ATM and manage your finances.",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

register_description.pack(pady=(0, 20))


# Full name
name_label = tk.Label(
    register_card,
    text="FULL NAME",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

name_label.pack(anchor="w", pady=(0, 5))


name_entry = tk.Entry(
    register_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

name_entry.pack(fill="x", ipady=9, pady=(0, 12))


# Phone number
phone_label = tk.Label(
    register_card,
    text="PHONE NUMBER",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

phone_label.pack(anchor="w", pady=(0, 5))


phone_entry = tk.Entry(
    register_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

phone_entry.pack(fill="x", ipady=9, pady=(0, 12))


# Create PIN
create_pin_label = tk.Label(
    register_card,
    text="CREATE 4-DIGIT PIN",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

create_pin_label.pack(anchor="w", pady=(0, 5))


create_pin_entry = tk.Entry(
    register_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    show="*"
)

create_pin_entry.pack(fill="x", ipady=9, pady=(0, 12))


# Confirm PIN
confirm_pin_label = tk.Label(
    register_card,
    text="CONFIRM PIN",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
)

confirm_pin_label.pack(anchor="w", pady=(0, 5))


confirm_pin_entry = tk.Entry(
    register_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    show="*"
)

confirm_pin_entry.pack(fill="x", ipady=9, pady=(0, 12))


register_message = tk.Label(
    register_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=ERROR
)

register_message.pack(anchor="w", pady=5)


# ==========================================
# DASHBOARD STRUCTURE
# ==========================================

sidebar = tk.Frame(
    dashboard_frame,
    bg=SIDEBAR,
    width=215
)

sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)


main_area = tk.Frame(
    dashboard_frame,
    bg=BG
)

main_area.grid(
    row=0,
    column=1,
    sticky="nsew"
)

main_area.grid_columnconfigure(0, weight=1)
main_area.grid_rowconfigure(1, weight=1)


# ==========================================
# SIDEBAR BRANDING
# ==========================================

brand = tk.Label(
    sidebar,
    text="◆  SMART ATM",
    font=("Arial", 17, "bold"),
    bg=SIDEBAR,
    fg=WHITE
)

brand.pack(anchor="w", padx=20, pady=(25, 30))


# ==========================================
# CUSTOMER PROFILE
# ==========================================

profile_card = tk.Frame(
    sidebar,
    bg=CARD,
    padx=12,
    pady=15
)

profile_card.pack(fill="x", padx=12)


profile_name = tk.Label(
    profile_card,
    text="Welcome back, Customer!",
    font=("Arial", 10, "bold"),
    bg=CARD,
    fg=WHITE
)

profile_name.pack(anchor="w")


profile_description = tk.Label(
    profile_card,
    text="Your banking overview",
    font=("Arial", 8),
    bg=CARD,
    fg=MUTED
)

profile_description.pack(anchor="w", pady=(5, 0))


# ==========================================
# SIDEBAR MENU
# ==========================================

menu_heading = tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 8, "bold"),
    bg=SIDEBAR,
    fg=MUTED
)

menu_heading.pack(anchor="w", padx=20, pady=(30, 12))


navigation_items = [
    ("▦", "Dashboard"),
    ("✧", "Smart ATM Insights"),
    ("▣", "Accounts"),
    ("↔", "Transactions"),
    ("▤", "Reports"),
    ("◈", "Investments"),
    ("▱", "Loans"),
    ("▧", "Taxes")
]


def create_navigation_button(icon, title):

    button = tk.Button(
        sidebar,
        text=f"  {icon}     {title}",
        font=("Arial", 10),
        bg=SIDEBAR,
        fg=MUTED,
        activebackground=CARD_LIGHT,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        anchor="w",
        cursor="hand2",
        padx=15,
        pady=12
    )

    button.pack(fill="x", padx=10, pady=2)

    return button


navigation_buttons = {}

for icon, title in navigation_items:

    button = create_navigation_button(
        icon,
        title
    )

    navigation_buttons[title] = button


# ==========================================
# LOAD CUSTOMER TRANSACTION HISTORY
# ==========================================

def refresh_transaction_history():

    if current_account_number is None:
        return

    accounts = main.load_accounts()

    if current_account_number not in accounts:
        return

    account = accounts[current_account_number]

    transactions = account.get("transactions", [])

    # Calculate deposit and withdrawal totals.
    total_deposits = sum(
        item["amount"]
        for item in transactions
        if item["type"].lower() == "deposit"
    )

    total_withdrawals = sum(
        item["amount"]
        for item in transactions
        if item["type"].lower() == "withdrawal"
    )

    # Update the totals on the Transactions page.
    total_deposits_value.config(
        text=f"₦{total_deposits:,.2f}"
    )

    total_withdrawals_value.config(
        text=f"₦{total_withdrawals:,.2f}"
    )

    # Remove previously displayed transaction rows.
    for widget in transactions_list_frame.winfo_children():
        widget.destroy()

    # Display a message if there are no transactions.
    if not transactions:

        empty_message = tk.Label(
            transactions_list_frame,
            text="No transactions recorded yet.",
            font=("Arial", 11),
            bg=CARD,
            fg=MUTED
        )

        empty_message.pack(pady=30)

        return

    # Display newest transactions first.
    sorted_transactions = sorted(
        transactions,
        key=lambda item: item.get("date", ""),
        reverse=True
    )

    for item in sorted_transactions:

        transaction_type = item.get("type", "Transaction")
        amount = item.get("amount", 0)
        date = item.get("date", "Date unavailable")

        row = tk.Frame(
            transactions_list_frame,
            bg=CARD,
            pady=12
        )

        row.pack(fill="x")

        row.grid_columnconfigure(0, weight=1)

        # Transaction name.
        name_label = tk.Label(
            row,
            text=transaction_type,
            font=("Arial", 10, "bold"),
            bg=CARD,
            fg=WHITE
        )

        name_label.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # Transaction date and time.
        date_label = tk.Label(
            row,
            text=date,
            font=("Arial", 8),
            bg=CARD,
            fg=MUTED
        )

        date_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(5, 0)
        )

        # Transaction amount and colour.
        if transaction_type.lower() == "deposit":

            amount_text = f"+₦{amount:,.2f}"
            amount_color = SUCCESS

        elif transaction_type.lower() == "withdrawal":

            amount_text = f"-₦{amount:,.2f}"
            amount_color = ERROR

        else:

            amount_text = f"₦{amount:,.2f}"
            amount_color = CYAN

        amount_label = tk.Label(
            row,
            text=amount_text,
            font=("Arial", 11, "bold"),
            bg=CARD,
            fg=amount_color
        )

        amount_label.grid(
            row=0,
            column=1,
            rowspan=2,
            sticky="e",
            padx=10
        )

        separator = tk.Frame(
            transactions_list_frame,
            bg=BORDER,
            height=1
        )

        separator.pack(fill="x")


# ==========================================
# PAGE NAVIGATION
# ==========================================

def show_dashboard():

    transactions_page.grid_remove()

    refresh_transaction_history()

    transactions_page.grid()
    

def show_transactions():

    dashboard_content.grid_remove()

    transactions_page.grid()


# Connect sidebar buttons
navigation_buttons["Dashboard"].config(
    command=show_dashboard
)

navigation_buttons["Transactions"].config(
    command=show_transactions
)

# ==========================================
# DASHBOARD HEADER
# ==========================================

header = tk.Frame(
    main_area,
    bg=BG,
    height=90
)

header.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=30,
    pady=(25, 10)
)

header.grid_columnconfigure(0, weight=1)


welcome_label = tk.Label(
    header,
    text="Dashboard Overview",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=WHITE
)

welcome_label.grid(row=0, column=0, sticky="w")


subtitle = tk.Label(
    header,
    text="Monitor your finances and banking activities",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
)

subtitle.grid(row=1, column=0, sticky="w", pady=(5, 0))


# ==========================================
# CURRENT ACCOUNT
# ==========================================

current_account_number = None


# ==========================================
# DASHBOARD CONTENT AREA
# ==========================================

dashboard_content = tk.Frame(
    main_area,
    bg=BG
)

dashboard_content.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=30,
    pady=15
)

dashboard_content.grid_columnconfigure(
    0,
    weight=1
)

dashboard_content.grid_columnconfigure(
    1,
    weight=1
)

dashboard_content.grid_columnconfigure(
    2,
    weight=1
)


# ==========================================
# TRANSACTIONS PAGE
# ==========================================

transactions_page = tk.Frame(
    main_area,
    bg=BG
)

transactions_page.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=30,
    pady=15
)

transactions_page.grid_remove()


# Page heading
transactions_heading = tk.Label(
    transactions_page,
    text="Transaction History",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=WHITE
)

transactions_heading.pack(anchor="w", pady=(0, 5))


transactions_subtitle = tk.Label(
    transactions_page,
    text="View all your deposits and withdrawals.",
    font=("Arial", 10),
    bg=BG,
    fg=MUTED
)

transactions_subtitle.pack(anchor="w", pady=(0, 25))


# ==========================================
# TRANSACTION TOTALS
# ==========================================

transaction_summary = tk.Frame(
    transactions_page,
    bg=BG
)

transaction_summary.pack(fill="x")

transaction_summary.grid_columnconfigure(0, weight=1)
transaction_summary.grid_columnconfigure(1, weight=1)


# Total deposits
deposits_card = tk.Frame(
    transaction_summary,
    bg=CARD,
    padx=20,
    pady=20
)

deposits_card.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=(0, 8)
)

deposits_title = tk.Label(
    deposits_card,
    text="TOTAL DEPOSITS",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=MUTED
)

deposits_title.pack(anchor="w")


total_deposits_value = tk.Label(
    deposits_card,
    text="₦0.00",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=SUCCESS
)

total_deposits_value.pack(anchor="w", pady=(10, 0))


# Total withdrawals
withdrawals_card = tk.Frame(
    transaction_summary,
    bg=CARD,
    padx=20,
    pady=20
)

withdrawals_card.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=(8, 0)
)

withdrawals_title = tk.Label(
    withdrawals_card,
    text="TOTAL WITHDRAWALS",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=MUTED
)

withdrawals_title.pack(anchor="w")


total_withdrawals_value = tk.Label(
    withdrawals_card,
    text="₦0.00",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=PURPLE
)

total_withdrawals_value.pack(anchor="w", pady=(10, 0))


# ==========================================
# ALL TRANSACTIONS SECTION
# ==========================================

history_card = tk.Frame(
    transactions_page,
    bg=CARD,
    padx=20,
    pady=20
)

history_card.pack(
    fill="both",
    expand=True,
    pady=(20, 0)
)


history_heading = tk.Label(
    history_card,
    text="All Transactions",
    font=("Arial", 14, "bold"),
    bg=CARD,
    fg=WHITE
)

history_heading.pack(anchor="w", pady=(0, 15))


transactions_list_frame = tk.Frame(
    history_card,
    bg=CARD
)

transactions_list_frame.pack(
    fill="both",
    expand=True
)


# ==========================================
# FINANCIAL SUMMARY CARDS
# ==========================================

def create_summary_card(parent, title, value, color):

    card = tk.Frame(
        parent,
        bg=CARD,
        padx=18,
        pady=20,
        highlightthickness=1,
        highlightbackground=BORDER
    )

    title_label = tk.Label(
        card,
        text=title,
        font=("Arial", 9, "bold"),
        bg=CARD,
        fg=MUTED
    )

    title_label.pack(anchor="w")

    value_label = tk.Label(
        card,
        text=value,
        font=("Arial", 19, "bold"),
        bg=CARD,
        fg=color
    )

    value_label.pack(anchor="w", pady=(12, 0))

    return card, value_label


# ==========================================
# AVAILABLE BALANCE CARD
# ==========================================

balance_card = tk.Frame(
    dashboard_content,
    bg=CARD,
    padx=25,
    pady=25,
    highlightthickness=1,
    highlightbackground=BORDER
)

balance_card.grid(
    row=0,
    column=0,
    columnspan=3,
    sticky="ew",
    padx=7,
    pady=7
)

balance_title = tk.Label(
    balance_card,
    text="AVAILABLE BALANCE",
    font=("Arial", 10, "bold"),
    bg=CARD,
    fg=MUTED
)

balance_title.pack(anchor="w")


# Balance display row
balance_display = tk.Frame(
    balance_card,
    bg=CARD
)

balance_display.pack(
    fill="x",
    pady=(12, 5)
)


balance_visible = True

balance_value = tk.Label(
    balance_display,
    text="₦0.00",
    font=("Arial", 28, "bold"),
    bg=CARD,
    fg=CYAN
)

balance_value.pack(side="left")


def toggle_balance():

    global balance_visible

    balance_visible = not balance_visible

    if balance_visible:
        balance_value.config(text="₦0.00")
        eye_button.config(text="◉")
    else:
        balance_value.config(text="••••••••")
        eye_button.config(text="◎")


eye_button = tk.Button(
    balance_display,
    text="◉",
    font=("Arial", 16),
    bg=CARD,
    fg=MUTED,
    activebackground=CARD,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=toggle_balance
)

eye_button.pack(side="left", padx=15)


balance_description = tk.Label(
    balance_card,
    text="Your current account balance",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

balance_description.pack(anchor="w")


balance_card.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=7,
    pady=7
)


# Total deposits card
deposit_card, deposit_value = create_summary_card(
    dashboard_content,
    "TOTAL DEPOSITS",
    "₦0.00",
    SUCCESS
)

deposit_card.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=7,
    pady=7
)


# Total withdrawals card
withdrawal_card, withdrawal_value = create_summary_card(
    dashboard_content,
    "TOTAL WITHDRAWALS",
    "₦0.00",
    PURPLE
)

withdrawal_card.grid(
    row=0,
    column=2,
    sticky="ew",
    padx=7,
    pady=7
)


# ==========================================
# LOGIN FUNCTION
# ==========================================

def handle_login():

    global current_account_number

    number = account_entry.get().strip()
    pin = pin_entry.get()

    if not number or not pin:
        login_message.config(
            text="Please enter your account number and PIN."
        )
        return

    accounts = main.load_accounts()

    if number not in accounts:
        login_message.config(
            text="Account number does not exist."
        )
        return

    account = accounts[number]

    # Support older accounts with plain PINs.
    if "pin" in account:

        if account["pin"] != pin:
            login_message.config(
                text="Incorrect account number or PIN."
            )
            return

        salt, hashed = main.hash_pin(pin)

        account["pin_salt"] = salt
        account["pin_hash"] = hashed

        del account["pin"]

        if not main.save_accounts(accounts):
            login_message.config(
                text="Could not update account security."
            )
            return

    # Verify hashed PINs.
    elif (
        "pin_salt" in account
        and "pin_hash" in account
        and main.verify_pin(account, pin)
    ):
        pass

    else:
        login_message.config(
            text="Incorrect account number or PIN."
        )
        return

    current_account_number = number

    profile_name.config(
        text=f"Welcome back, {account['name']}!"
    )

    profile_description.config(
        text=f"Account: {number}"
    )

    welcome_label.config(
        text=f"Welcome back, {account['name']}!"
    )

    subtitle.config(
        text="Here is your personal banking overview."
    )

    account_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)
    login_message.config(text="")

    login_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )


# ==========================================
# CREATE ACCOUNT FUNCTION
# ==========================================

def handle_registration():

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    pin = create_pin_entry.get()
    confirm_pin = confirm_pin_entry.get()

    # Check that no field is empty.
    if not name or not phone or not pin or not confirm_pin:
        register_message.config(
            text="Please complete all fields.",
            fg=ERROR
        )
        return

    # Check the phone number.
    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        register_message.config(
            text="Enter a valid phone number.",
            fg=ERROR
        )
        return

    # Check the PIN.
    if len(pin) != 4 or not pin.isdigit():
        register_message.config(
            text="PIN must contain exactly 4 digits.",
            fg=ERROR
        )
        return

    # Check PIN confirmation.
    if pin != confirm_pin:
        register_message.config(
            text="Your PINs do not match.",
            fg=ERROR
        )
        return

    # Load existing customer accounts.
    accounts = main.load_accounts()

    # Generate a unique account number.
    number = main.generate_account_number(accounts)

    # Securely hash the customer's PIN.
    salt, hashed = main.hash_pin(pin)

    # Store the new customer.
    accounts[number] = {
        "name": name,
        "phone": phone,
        "pin_salt": salt,
        "pin_hash": hashed,
        "balance": 0,
        "transactions": []
    }

    # Save the new account.
    if not main.save_accounts(accounts):
        register_message.config(
            text="Account could not be saved. Try again.",
            fg=ERROR
        )
        return

    # Show the generated account number.
    register_message.config(
        text=f"Account created successfully!\nYour account number is: {number}",
        fg=SUCCESS
    )

    # Prepare the login screen with the new account number.
    account_entry.delete(0, tk.END)
    account_entry.insert(0, number)

    pin_entry.delete(0, tk.END)

    # Clear registration fields.
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    create_pin_entry.delete(0, tk.END)
    confirm_pin_entry.delete(0, tk.END)


# ==========================================
# LOGOUT FUNCTION
# ==========================================

def logout():

    global current_account_number

    current_account_number = None

    pin_entry.delete(0, tk.END)
    login_message.config(text="")

    dashboard_frame.pack_forget()

    login_frame.pack(
        fill="both",
        expand=True
    )


# ==========================================
# LOGIN BUTTON
# ==========================================

login_button = tk.Button(
    login_card,
    text="SIGN IN",
    font=("Arial", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_login
)

login_button.pack(fill="x", ipady=12, pady=(5, 12))


# ==========================================
# OPEN ACCOUNT BUTTON
# ==========================================

open_account_button = tk.Button(
    login_card,
    text="CREATE A NEW ACCOUNT",
    font=("Arial", 10, "bold"),
    bg=CARD_LIGHT,
    fg=CYAN,
    activebackground=SIDEBAR,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=show_register
)

open_account_button.pack(fill="x", ipady=10, pady=(0, 15))


security_message = tk.Label(
    login_card,
    text="SECURE LOCAL BANKING SIMULATION",
    font=("Arial", 8, "bold"),
    bg=CARD,
    fg=MUTED
)

security_message.pack(pady=(5, 0))


# ==========================================
# REGISTRATION BUTTON
# ==========================================

register_button = tk.Button(
    register_card,
    text="CREATE ACCOUNT",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_registration
)

register_button.pack(fill="x", ipady=10, pady=(8, 10))


back_to_login_button = tk.Button(
    register_card,
    text="ALREADY HAVE AN ACCOUNT? SIGN IN",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=CYAN,
    activebackground=CARD,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=show_login
)

back_to_login_button.pack(pady=(5, 0))


# ==========================================
# LOGOUT BUTTON
# ==========================================

logout_button = tk.Button(
    sidebar,
    text="  ↪     Logout",
    font=("Arial", 10, "bold"),
    bg=SIDEBAR,
    fg=ERROR,
    activebackground=CARD_LIGHT,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    anchor="w",
    cursor="hand2",
    padx=15,
    pady=12,
    command=logout
)

logout_button.pack(
    side="bottom",
    fill="x",
    padx=10,
    pady=20
)


# ==========================================
# START APPLICATION
# ==========================================

show_login()

root.mainloop()
