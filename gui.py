
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import secrets

import main
import banks


# =========================================================
# SMART ATM - PREMIUM DARK BANKING SYSTEM
# =========================================================

root = tk.Tk()
root.title("Smart ATM | Digital Banking")
root.geometry("1250x780")
root.minsize(1100, 700)
root.configure(bg="#090B16")


# =========================================================
# COLOUR PALETTE
# =========================================================

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


# =========================================================
# CURRENT ACCOUNT
# =========================================================

current_account_number = None
balance_visible = True


def get_current_account():

    if current_account_number is None:
        return None

    accounts = main.load_accounts()

    return accounts.get(current_account_number)


def money(value):
    return f"₦{value:,.2f}"


def save_updated_accounts(accounts):

    if not main.save_accounts(accounts):

        messagebox.showerror(
            "Save error",
            "Your changes could not be saved. Please try again."
        )

        return False

    return True


# =========================================================
# ROOT SCREEN CONTAINERS
# =========================================================

login_frame = tk.Frame(root, bg=BG)
register_frame = tk.Frame(root, bg=BG)
app_frame = tk.Frame(root, bg=BG)

app_frame.grid_rowconfigure(0, weight=1)
app_frame.grid_columnconfigure(1, weight=1)


def show_login():

    register_frame.pack_forget()
    app_frame.pack_forget()

    login_frame.pack(fill="both", expand=True)


def show_register():

    login_frame.pack_forget()
    app_frame.pack_forget()

    register_frame.pack(fill="both", expand=True)


# =========================================================
# LOGIN SCREEN
# =========================================================

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


tk.Label(
    login_card,
    text="◆  SMART ATM",
    font=("Arial", 23, "bold"),
    bg=CARD,
    fg=WHITE
).pack(pady=(5, 12))


tk.Label(
    login_card,
    text="Your finances. Your control.",
    font=("Arial", 10),
    bg=CARD,
    fg=MUTED
).pack(pady=(0, 30))


tk.Label(
    login_card,
    text="Welcome Back",
    font=("Arial", 21, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w")


tk.Label(
    login_card,
    text="Sign in to access your banking dashboard.",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
).pack(anchor="w", pady=(7, 25))


tk.Label(
    login_card,
    text="ACCOUNT NUMBER",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 8))


account_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    highlightthickness=1,
    highlightbackground=BORDER
)

account_entry.pack(fill="x", ipady=12, pady=(0, 20))


tk.Label(
    login_card,
    text="4-DIGIT PIN",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 8))


pin_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    show="*",
    highlightthickness=1,
    highlightbackground=BORDER
)

pin_entry.pack(fill="x", ipady=12, pady=(0, 15))


login_message = tk.Label(
    login_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=ERROR
)

login_message.pack(anchor="w", pady=(0, 10))


# =========================================================
# REGISTRATION SCREEN
# =========================================================

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


tk.Label(
    register_card,
    text="◆  SMART ATM",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=WHITE
).pack(pady=(5, 10))


tk.Label(
    register_card,
    text="Create Your Account",
    font=("Arial", 21, "bold"),
    bg=CARD,
    fg=WHITE
).pack(pady=(10, 5))


tk.Label(
    register_card,
    text="Join Smart ATM and manage your finances.",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
).pack(pady=(0, 20))


def make_entry(parent, label, show=None):

    tk.Label(
        parent,
        text=label,
        font=("Arial", 9, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(anchor="w", pady=(0, 5))

    field = tk.Entry(
        parent,
        font=("Arial", 11),
        bg=CARD_LIGHT,
        fg=WHITE,
        insertbackground=WHITE,
        relief="flat",
        show=show
    )

    field.pack(fill="x", ipady=9, pady=(0, 12))

    return field


name_entry = make_entry(register_card, "FULL NAME")
phone_entry = make_entry(register_card, "PHONE NUMBER")
create_pin_entry = make_entry(register_card, "CREATE 4-DIGIT PIN", "*")
confirm_pin_entry = make_entry(register_card, "CONFIRM PIN", "*")


register_message = tk.Label(
    register_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=ERROR,
    justify="left",
    wraplength=350
)

register_message.pack(anchor="w", pady=5)


# =========================================================
# MAIN APPLICATION LAYOUT
# =========================================================

sidebar = tk.Frame(
    app_frame,
    bg=SIDEBAR,
    width=215
)

sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)


main_area = tk.Frame(
    app_frame,
    bg=BG
)

main_area.grid(
    row=0,
    column=1,
    sticky="nsew"
)

main_area.grid_rowconfigure(0, weight=1)
main_area.grid_columnconfigure(0, weight=1)


# =========================================================
# SIDEBAR BRANDING
# =========================================================

tk.Label(
    sidebar,
    text="◆  SMART ATM",
    font=("Arial", 17, "bold"),
    bg=SIDEBAR,
    fg=WHITE
).pack(anchor="w", padx=20, pady=(25, 30))


# =========================================================
# CUSTOMER PROFILE
# =========================================================

profile_card = tk.Frame(
    sidebar,
    bg=CARD,
    padx=12,
    pady=15
)

profile_card.pack(fill="x", padx=12)


profile_name = tk.Label(
    profile_card,
    text="Welcome, Customer!",
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


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 8, "bold"),
    bg=SIDEBAR,
    fg=MUTED
).pack(anchor="w", padx=20, pady=(30, 12))


navigation_items = [
    ("▦", "Dashboard"),
    ("↔", "Transactions"),
    ("＋", "Deposit"),
    ("－", "Withdraw"),
    ("⇄", "Send Money")
]


navigation_buttons = {}


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


for icon, title in navigation_items:

    navigation_buttons[title] = create_navigation_button(
        icon,
        title
    )


# =========================================================
# PAGE CONTAINER
# Every page occupies the same position.
# Only one page is displayed at a time.
# =========================================================

pages_container = tk.Frame(
    main_area,
    bg=BG
)

pages_container.grid(
    row=0,
    column=0,
    sticky="nsew"
)

pages_container.grid_rowconfigure(0, weight=1)
pages_container.grid_columnconfigure(0, weight=1)


dashboard_page = tk.Frame(pages_container, bg=BG)
transactions_page = tk.Frame(pages_container, bg=BG)
deposit_page = tk.Frame(pages_container, bg=BG)
withdraw_page = tk.Frame(pages_container, bg=BG)
transfer_page = tk.Frame(pages_container, bg=BG)


all_pages = {
    "Dashboard": dashboard_page,
    "Transactions": transactions_page,
    "Deposit": deposit_page,
    "Withdraw": withdraw_page,
    "Send Money": transfer_page
}


def show_page(page_name):

    # Hide every page first.
    for page in all_pages.values():

        page.grid_remove()

    # Display only the selected page.
    all_pages[page_name].grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    if page_name == "Dashboard":

        refresh_dashboard()

    elif page_name == "Transactions":

        refresh_transaction_history()


# =========================================================
# PAGE HEADING FUNCTION
# =========================================================

def page_heading(parent, heading, description):

    tk.Label(
        parent,
        text=heading,
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(anchor="w", pady=(25, 5), padx=30)

    tk.Label(
        parent,
        text=description,
        font=("Arial", 10),
        bg=BG,
        fg=MUTED
    ).pack(anchor="w", padx=30, pady=(0, 22))


# =========================================================
# DASHBOARD PAGE
# =========================================================

page_heading(
    dashboard_page,
    "Dashboard",
    "Here is your personal banking overview."
)


dashboard_body = tk.Frame(
    dashboard_page,
    bg=BG
)

dashboard_body.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 25)
)


# =========================================================
# AVAILABLE BALANCE CARD
# =========================================================

balance_card = tk.Frame(
    dashboard_body,
    bg=CARD,
    padx=25,
    pady=25,
    highlightthickness=1,
    highlightbackground=BORDER
)

balance_card.pack(
    fill="x",
    pady=(0, 22)
)


balance_top = tk.Frame(
    balance_card,
    bg=CARD
)

balance_top.pack(fill="x")


tk.Label(
    balance_top,
    text="AVAILABLE BALANCE",
    font=("Arial", 10, "bold"),
    bg=CARD,
    fg=MUTED
).pack(side="left")


balance_display = tk.Frame(
    balance_card,
    bg=CARD
)

balance_display.pack(
    fill="x",
    pady=(12, 5)
)


balance_value = tk.Label(
    balance_display,
    text="₦0.00",
    font=("Arial", 29, "bold"),
    bg=CARD,
    fg=CYAN
)

balance_value.pack(side="left")


def toggle_balance():

    global balance_visible

    balance_visible = not balance_visible

    refresh_balance_display()


eye_button = tk.Button(
    balance_display,
    text="◉",
    font=("Arial", 15),
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


tk.Label(
    balance_card,
    text="Your current account balance",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")


# =========================================================
# TRANSACTION HISTORY LINK ON DASHBOARD
# =========================================================

history_link_row = tk.Frame(
    dashboard_body,
    bg=BG
)

history_link_row.pack(
    fill="x",
    pady=(5, 5)
)


tk.Label(
    history_link_row,
    text="Transaction History",
    font=("Arial", 15, "bold"),
    bg=BG,
    fg=WHITE
).pack(side="left")


view_all_button = tk.Button(
    history_link_row,
    text="View all  →",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=CYAN,
    activebackground=BG,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=lambda: show_page("Transactions")
)

view_all_button.pack(side="right")


tk.Label(
    dashboard_body,
    text="View your deposits, withdrawals and transfers.",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
).pack(anchor="w", pady=(0, 12))


# =========================================================
# RECENT TRANSACTIONS ON DASHBOARD
# =========================================================

recent_card = tk.Frame(
    dashboard_body,
    bg=CARD,
    padx=20,
    pady=18
)

recent_card.pack(
    fill="both",
    expand=True
)


tk.Label(
    recent_card,
    text="Recent Transactions",
    font=("Arial", 13, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(0, 12))


recent_list_frame = tk.Frame(
    recent_card,
    bg=CARD
)

recent_list_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# REFRESH BALANCE DISPLAY
# =========================================================

def refresh_balance_display():

    account = get_current_account()

    balance = account.get("balance", 0) if account else 0

    if balance_visible:

        balance_value.config(text=money(balance))
        eye_button.config(text="◉")

    else:

        balance_value.config(text="••••••••")
        eye_button.config(text="◎")


# =========================================================
# TRANSACTION ROW DESIGN
# =========================================================

def create_transaction_row(parent, item):

    row = tk.Frame(
        parent,
        bg=CARD,
        pady=10
    )

    row.pack(fill="x")


    left = tk.Frame(
        row,
        bg=CARD
    )

    left.pack(
        side="left",
        fill="x",
        expand=True
    )


    transaction_type = item.get("type", "Transaction")
    date = item.get("date", "Date unavailable")
    amount = item.get("amount", 0)

    title = transaction_type


    if transaction_type.lower() == "transfer":

        bank_name = item.get("bank", "")
        beneficiary = item.get("beneficiary", "")

        if bank_name or beneficiary:

            title = f"Transfer • {beneficiary or 'Beneficiary'}"

            if bank_name:
                title += f" ({bank_name})"


    tk.Label(
        left,
        text=title,
        font=("Arial", 10, "bold"),
        bg=CARD,
        fg=WHITE,
        anchor="w"
    ).pack(anchor="w")


    tk.Label(
        left,
        text=date,
        font=("Arial", 8),
        bg=CARD,
        fg=MUTED,
        anchor="w"
    ).pack(anchor="w", pady=(4, 0))


    if transaction_type.lower() == "deposit":

        amount_text = f"+{money(amount)}"
        amount_color = SUCCESS

    elif transaction_type.lower() in ("withdrawal", "transfer"):

        amount_text = f"-{money(amount)}"
        amount_color = ERROR

    else:

        amount_text = money(amount)
        amount_color = CYAN


    tk.Label(
        row,
        text=amount_text,
        font=("Arial", 10, "bold"),
        bg=CARD,
        fg=amount_color
    ).pack(side="right", padx=(10, 0))


    tk.Frame(
        parent,
        bg=BORDER,
        height=1
    ).pack(fill="x")


# =========================================================
# REFRESH DASHBOARD
# =========================================================

def refresh_dashboard():

    refresh_balance_display()

    for widget in recent_list_frame.winfo_children():

        widget.destroy()

    account = get_current_account()

    if not account:
        return

    transactions = account.get("transactions", [])

    newest = sorted(
        transactions,
        key=lambda item: item.get("date", ""),
        reverse=True
    )[:5]


    if not newest:

        tk.Label(
            recent_list_frame,
            text="No transactions yet. Your activity will appear here.",
            font=("Arial", 10),
            bg=CARD,
            fg=MUTED
        ).pack(anchor="w", pady=15)

        return


    for item in newest:

        create_transaction_row(
            recent_list_frame,
            item
        )


# =========================================================
# TRANSACTION HISTORY PAGE
# =========================================================

page_heading(
    transactions_page,
    "Transaction History",
    "View all your deposits, withdrawals and transfers."
)


transaction_body = tk.Frame(
    transactions_page,
    bg=BG
)

transaction_body.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 25)
)


# =========================================================
# DEPOSIT AND WITHDRAWAL TOTALS
# =========================================================

totals_row = tk.Frame(
    transaction_body,
    bg=BG
)

totals_row.pack(fill="x")

totals_row.grid_columnconfigure(0, weight=1)
totals_row.grid_columnconfigure(1, weight=1)


deposits_card = tk.Frame(
    totals_row,
    bg=CARD,
    padx=20,
    pady=18
)

deposits_card.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=(0, 8)
)


withdrawals_card = tk.Frame(
    totals_row,
    bg=CARD,
    padx=20,
    pady=18
)

withdrawals_card.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=(8, 0)
)


tk.Label(
    deposits_card,
    text="TOTAL DEPOSITS",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")


total_deposits_value = tk.Label(
    deposits_card,
    text="₦0.00",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=SUCCESS
)

total_deposits_value.pack(anchor="w", pady=(10, 0))


tk.Label(
    withdrawals_card,
    text="TOTAL WITHDRAWALS",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w")


total_withdrawals_value = tk.Label(
    withdrawals_card,
    text="₦0.00",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=PURPLE
)

total_withdrawals_value.pack(anchor="w", pady=(10, 0))


# =========================================================
# ALL TRANSACTIONS SECTION
# =========================================================

history_card = tk.Frame(
    transaction_body,
    bg=CARD,
    padx=20,
    pady=18
)

history_card.pack(
    fill="both",
    expand=True,
    pady=(18, 0)
)


tk.Label(
    history_card,
    text="All Transactions",
    font=("Arial", 14, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(0, 12))


transactions_list_frame = tk.Frame(
    history_card,
    bg=CARD
)

transactions_list_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# REFRESH TRANSACTION HISTORY
# =========================================================

def refresh_transaction_history():

    account = get_current_account()

    if not account:
        return

    transactions = account.get("transactions", [])


    total_deposits = sum(
        item.get("amount", 0)
        for item in transactions
        if item.get("type", "").lower() == "deposit"
    )


    total_withdrawals = sum(
        item.get("amount", 0)
        for item in transactions
        if item.get("type", "").lower() == "withdrawal"
    )


    total_deposits_value.config(
        text=money(total_deposits)
    )

    total_withdrawals_value.config(
        text=money(total_withdrawals)
    )


    for widget in transactions_list_frame.winfo_children():

        widget.destroy()


    newest = sorted(
        transactions,
        key=lambda item: item.get("date", ""),
        reverse=True
    )


    if not newest:

        tk.Label(
            transactions_list_frame,
            text="No transactions recorded yet.",
            font=("Arial", 10),
            bg=CARD,
            fg=MUTED
        ).pack(anchor="w", pady=20)

        return


    for item in newest:

        create_transaction_row(
            transactions_list_frame,
            item
        )


# =========================================================
# DEPOSIT PAGE
# =========================================================

page_heading(
    deposit_page,
    "Deposit Money",
    "Add money to your Smart ATM simulation account."
)


deposit_card = tk.Frame(
    deposit_page,
    bg=CARD,
    padx=25,
    pady=25
)

deposit_card.pack(fill="x", padx=30)


tk.Label(
    deposit_card,
    text="AMOUNT (₦)",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 8))


deposit_amount_entry = tk.Entry(
    deposit_card,
    font=("Arial", 13),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

deposit_amount_entry.pack(
    fill="x",
    ipady=12,
    pady=(0, 15)
)


deposit_message = tk.Label(
    deposit_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

deposit_message.pack(anchor="w", pady=(0, 10))


def handle_deposit():

    raw_amount = deposit_amount_entry.get().strip()

    try:

        amount = float(raw_amount)

        if amount <= 0:
            raise ValueError

    except ValueError:

        deposit_message.config(
            text="Enter a valid amount greater than zero.",
            fg=ERROR
        )

        return


    accounts = main.load_accounts()

    account = accounts.get(current_account_number)

    if not account:

        deposit_message.config(
            text="Account could not be found.",
            fg=ERROR
        )

        return


    account["balance"] = float(account.get("balance", 0)) + amount

    account.setdefault("transactions", []).append({
        "type": "Deposit",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


    if save_updated_accounts(accounts):

        deposit_amount_entry.delete(0, tk.END)

        deposit_message.config(
            text=f"Deposit recorded: {money(amount)}",
            fg=SUCCESS
        )

        refresh_dashboard()
        refresh_transaction_history()


tk.Button(
    deposit_card,
    text="ADD DEPOSIT",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_deposit
).pack(fill="x", ipady=11)


# =========================================================
# WITHDRAW PAGE
# =========================================================

page_heading(
    withdraw_page,
    "Withdraw Money",
    "Withdraw money from your Smart ATM simulation account."
)


withdraw_card = tk.Frame(
    withdraw_page,
    bg=CARD,
    padx=25,
    pady=25
)

withdraw_card.pack(fill="x", padx=30)


tk.Label(
    withdraw_card,
    text="AMOUNT (₦)",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 8))


withdraw_amount_entry = tk.Entry(
    withdraw_card,
    font=("Arial", 13),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

withdraw_amount_entry.pack(
    fill="x",
    ipady=12,
    pady=(0, 15)
)


withdraw_message = tk.Label(
    withdraw_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED
)

withdraw_message.pack(anchor="w", pady=(0, 10))


def handle_withdrawal():

    raw_amount = withdraw_amount_entry.get().strip()

    try:

        amount = float(raw_amount)

        if amount <= 0:
            raise ValueError

    except ValueError:

        withdraw_message.config(
            text="Enter a valid amount greater than zero.",
            fg=ERROR
        )

        return


    accounts = main.load_accounts()

    account = accounts.get(current_account_number)

    if not account:

        withdraw_message.config(
            text="Account could not be found.",
            fg=ERROR
        )

        return


    balance = float(account.get("balance", 0))

    if amount > balance:

        withdraw_message.config(
            text="Insufficient balance.",
            fg=ERROR
        )

        return


    account["balance"] = balance - amount

    account.setdefault("transactions", []).append({
        "type": "Withdrawal",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


    if save_updated_accounts(accounts):

        withdraw_amount_entry.delete(0, tk.END)

        withdraw_message.config(
            text=f"Withdrawal recorded: {money(amount)}",
            fg=SUCCESS
        )

        refresh_dashboard()
        refresh_transaction_history()


tk.Button(
    withdraw_card,
    text="WITHDRAW",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_withdrawal
).pack(fill="x", ipady=11)


# =========================================================
# SEND MONEY PAGE
# =========================================================

page_heading(
    transfer_page,
    "Send Money",
    "Choose a bank, enter beneficiary details and record a simulated transfer."
)


transfer_card = tk.Frame(
    transfer_page,
    bg=CARD,
    padx=25,
    pady=22
)

transfer_card.pack(fill="x", padx=30)


tk.Label(
    transfer_card,
    text="SEARCH / SELECT BANK",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 7))


bank_options = sorted(
    set(banks.BANKS),
    key=str.lower
)


bank_search = ttk.Combobox(
    transfer_card,
    values=bank_options,
    font=("Arial", 11)
)

bank_search.pack(
    fill="x",
    ipady=7,
    pady=(0, 14)
)

bank_search.configure(state="normal")


def filter_banks(event=None):

    search_text = bank_search.get().strip().lower()

    matches = [
        bank
        for bank in bank_options
        if search_text in bank.lower()
    ]

    bank_search["values"] = matches if matches else bank_options

    if search_text and matches:
        bank_search.event_generate("<Down>")


bank_search.bind(
    "<KeyRelease>",
    filter_banks
)


tk.Label(
    transfer_card,
    text="BENEFICIARY FULL NAME",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 7))


beneficiary_entry = tk.Entry(
    transfer_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

beneficiary_entry.pack(
    fill="x",
    ipady=10,
    pady=(0, 14)
)


tk.Label(
    transfer_card,
    text="BENEFICIARY ACCOUNT NUMBER",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 7))


beneficiary_account_entry = tk.Entry(
    transfer_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

beneficiary_account_entry.pack(
    fill="x",
    ipady=10,
    pady=(0, 14)
)


tk.Label(
    transfer_card,
    text="AMOUNT (₦)",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", pady=(0, 7))


transfer_amount_entry = tk.Entry(
    transfer_card,
    font=("Arial", 11),
    bg=CARD_LIGHT,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

transfer_amount_entry.pack(
    fill="x",
    ipady=10,
    pady=(0, 14)
)


transfer_message = tk.Label(
    transfer_card,
    text="",
    font=("Arial", 9),
    bg=CARD,
    fg=MUTED,
    justify="left",
    wraplength=700
)

transfer_message.pack(anchor="w", pady=(0, 12))


tk.Label(
    transfer_card,
    text="Demo only: this records a simulated transfer and does not send money through a real bank network.",
    font=("Arial", 8),
    bg=CARD,
    fg=MUTED,
    wraplength=750,
    justify="left"
).pack(anchor="w", pady=(0, 12))


# =========================================================
# HANDLE BANK TRANSFER
# =========================================================

def handle_transfer():

    bank_name = bank_search.get().strip()
    beneficiary = beneficiary_entry.get().strip()
    beneficiary_number = beneficiary_account_entry.get().strip()
    raw_amount = transfer_amount_entry.get().strip()


    if not bank_name or bank_name not in bank_options:

        transfer_message.config(
            text="Please select a bank or payment provider from the list.",
            fg=ERROR
        )

        return


    if not beneficiary:

        transfer_message.config(
            text="Enter the beneficiary's name.",
            fg=ERROR
        )

        return


    if not beneficiary_number.isdigit() or not 8 <= len(beneficiary_number) <= 12:

        transfer_message.config(
            text="Enter a valid beneficiary account number (8–12 digits).",
            fg=ERROR
        )

        return


    try:

        amount = float(raw_amount)

        if amount <= 0:
            raise ValueError

    except ValueError:

        transfer_message.config(
            text="Enter a valid amount greater than zero.",
            fg=ERROR
        )

        return


    accounts = main.load_accounts()

    account = accounts.get(current_account_number)

    if not account:

        transfer_message.config(
            text="Your account could not be found.",
            fg=ERROR
        )

        return


    balance = float(account.get("balance", 0))

    if amount > balance:

        transfer_message.config(
            text="Insufficient balance for this transfer.",
            fg=ERROR
        )

        return


    confirmed = messagebox.askyesno(
        "Confirm simulated transfer",
        f"Record this simulated transfer?\n\n"
        f"Bank: {bank_name}\n"
        f"Beneficiary: {beneficiary}\n"
        f"Account number: {beneficiary_number}\n"
        f"Amount: {money(amount)}\n\n"
        "This will deduct the amount from your local demo balance. "
        "It will NOT credit a real external bank account."
    )


    if not confirmed:
        return


    entered_pin = simpledialog.askstring(
        "Transfer Security",
        "Enter your 4-digit PIN to authorise this transfer:",
        show="*"
    )

    if entered_pin is None:
        return

    if not main.verify_pin(account, entered_pin):

        messagebox.showerror(
            "Security Verification Failed",
            "Incorrect PIN. Your transfer was cancelled."
        )

        return

    reference = "SATM" + secrets.token_hex(4).upper()


    account["balance"] = balance - amount

    account.setdefault("transactions", []).append({
        "type": "Transfer",
        "amount": amount,
        "bank": bank_name,
        "beneficiary": beneficiary,
        "beneficiary_account": beneficiary_number,
        "reference": reference,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Simulated"
    })


    if save_updated_accounts(accounts):

        beneficiary_entry.delete(0, tk.END)
        beneficiary_account_entry.delete(0, tk.END)
        transfer_amount_entry.delete(0, tk.END)

        transfer_message.config(
            text=f"Simulated transfer recorded successfully. Reference: {reference}",
            fg=SUCCESS
        )

        refresh_dashboard()
        refresh_transaction_history()


tk.Button(
    transfer_card,
    text="REVIEW AND SEND",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_transfer
).pack(fill="x", ipady=11)


# =========================================================
# LOGIN FUNCTION
# =========================================================

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


    # Support older accounts with plain-text PINs.
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

    account_entry.delete(0, tk.END)
    pin_entry.delete(0, tk.END)

    login_message.config(text="")

    login_frame.pack_forget()

    app_frame.pack(
        fill="both",
        expand=True
    )

    show_page("Dashboard")


# =========================================================
# REGISTRATION FUNCTION
# =========================================================

def handle_registration():

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    pin = create_pin_entry.get()
    confirm_pin = confirm_pin_entry.get()


    if not name or not phone or not pin or not confirm_pin:

        register_message.config(
            text="Please complete all fields.",
            fg=ERROR
        )

        return


    if not phone.isdigit() or not 10 <= len(phone) <= 15:

        register_message.config(
            text="Enter a valid phone number.",
            fg=ERROR
        )

        return


    if len(pin) != 4 or not pin.isdigit():

        register_message.config(
            text="PIN must contain exactly 4 digits.",
            fg=ERROR
        )

        return


    if pin != confirm_pin:

        register_message.config(
            text="Your PINs do not match.",
            fg=ERROR
        )

        return


    accounts = main.load_accounts()

    number = main.generate_account_number(accounts)

    salt, hashed = main.hash_pin(pin)


    accounts[number] = {
        "name": name,
        "phone": phone,
        "pin_salt": salt,
        "pin_hash": hashed,
        "balance": 0,
        "transactions": []
    }


    if not main.save_accounts(accounts):

        register_message.config(
            text="Account could not be saved. Try again.",
            fg=ERROR
        )

        return


    register_message.config(
        text=f"Account created successfully!\nYour account number is: {number}",
        fg=SUCCESS
    )


    account_entry.delete(0, tk.END)
    account_entry.insert(0, number)

    pin_entry.delete(0, tk.END)

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    create_pin_entry.delete(0, tk.END)
    confirm_pin_entry.delete(0, tk.END)


# =========================================================
# LOGOUT FUNCTION
# =========================================================

def logout():

    global current_account_number
    global balance_visible

    current_account_number = None
    balance_visible = True

    pin_entry.delete(0, tk.END)

    login_message.config(text="")

    app_frame.pack_forget()

    show_login()


# =========================================================
# LOGIN BUTTON
# =========================================================

tk.Button(
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
).pack(fill="x", ipady=12, pady=(5, 12))


# =========================================================
# OPEN ACCOUNT BUTTON
# =========================================================

tk.Button(
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
).pack(fill="x", ipady=10, pady=(0, 15))


tk.Label(
    login_card,
    text="SECURE LOCAL BANKING SIMULATION",
    font=("Arial", 8, "bold"),
    bg=CARD,
    fg=MUTED
).pack(pady=(5, 0))


# =========================================================
# REGISTRATION BUTTON
# =========================================================

tk.Button(
    register_card,
    text="CREATE ACCOUNT",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=PURPLE,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=handle_registration
).pack(fill="x", ipady=10, pady=(8, 10))


tk.Button(
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
).pack(pady=(5, 0))


# =========================================================
# LOGOUT BUTTON
# =========================================================

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


# =========================================================
# CONNECT SIDEBAR BUTTONS
# =========================================================

for page_name, button in navigation_buttons.items():

    button.config(
        command=lambda name=page_name: show_page(name)
    )


# =========================================================
# START APPLICATION
# =========================================================

show_login()

root.mainloop()
