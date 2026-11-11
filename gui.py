
import tkinter as tk

# =====================================
# MAIN APPLICATION WINDOW
# =====================================

root = tk.Tk()

root.title("SMART ATM | Digital Banking")
root.geometry("1100x700")
root.minsize(950, 600)
root.configure(bg="#F4F7FC")


# =====================================
# COLOUR PALETTE
# =====================================

NAVY = "#14213D"
BLUE = "#2563EB"
WHITE = "#FFFFFF"
BACKGROUND = "#F4F7FC"
TEXT = "#263449"
MUTED = "#718096"


# =====================================
# MAIN WINDOW LAYOUT
# =====================================

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


# =====================================
# SIDEBAR
# =====================================

sidebar = tk.Frame(
    root,
    bg=NAVY,
    width=240
)

sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)


# SMART ATM BRANDING

brand_label = tk.Label(
    sidebar,
    text="SMART ATM",
    font=("Arial", 22, "bold"),
    bg=NAVY,
    fg=WHITE
)

brand_label.pack(pady=(35, 5))


subtitle_label = tk.Label(
    sidebar,
    text="DIGITAL BANKING",
    font=("Arial", 9),
    bg=NAVY,
    fg="#AAB8D0"
)

subtitle_label.pack(pady=2)


# =====================================
# MAIN DASHBOARD AREA
# =====================================

main_area = tk.Frame(
    root,
    bg=BACKGROUND
)

main_area.grid(row=0, column=1, sticky="nsew")

# =====================================
# DASHBOARD HEADER
# =====================================

header = tk.Frame(
    main_area,
    bg=BACKGROUND
)

header.pack(fill="x", padx=35, pady=30)


# Welcome message

welcome_label = tk.Label(
    header,
    text="Welcome to Smart ATM",
    font=("Arial", 24, "bold"),
    bg=BACKGROUND,
    fg=TEXT
)

welcome_label.pack(anchor="w")


# Dashboard description

description_label = tk.Label(
    header,
    text="Manage your money securely and conveniently.",
    font=("Arial", 11),
    bg=BACKGROUND,
    fg=MUTED
)

description_label.pack(anchor="w", pady=(5, 0))
# =====================================
# ACCOUNT BALANCE CARD
# =====================================

balance_card = tk.Frame(
    main_area,
    bg=BLUE,
    height=190
)

balance_card.pack(
    fill="x",
    padx=35,
    pady=20
)

balance_card.pack_propagate(False)

balance_title = tk.Label(
    balance_card,
    text="TOTAL ACCOUNT BALANCE",
    font=("Arial", 10, "bold"),
    bg=BLUE,
    fg="#DCE8FF"
)

balance_title.pack(anchor="w", padx=25, pady=(22, 5))

balance_amount = tk.Label(
    balance_card,
    text="₦0.00",
    font=("Arial", 30, "bold"),
    bg=BLUE,
    fg=WHITE
)

balance_amount.pack(anchor="w", padx=25)

account_holder = tk.Label(
    balance_card,
    text="ACCOUNT HOLDER: SMART ATM CUSTOMER",
    font=("Arial", 9),
    bg=BLUE,
    fg="#DCE8FF"
)

account_holder.pack(anchor="w", padx=25, pady=(8, 0))

# QUICK ACTIONS SECTION

quick_actions_title = tk.Label(
    main_area,
    text="Quick Actions",
    font=("Arial", 17, "bold"),
    bg=BACKGROUND,
    fg=TEXT
)

quick_actions_title.pack(
    anchor="w",
    padx=35,
    pady=(20, 10)
)

# QUICK ACTIONS CONTAINER

quick_actions_frame = tk.Frame(
    main_area,
    bg=BACKGROUND
)

quick_actions_frame.pack(
    fill="x",
    padx=35,
    pady=10
)

# DEPOSIT BUTTON

deposit_button = tk.Button(
    quick_actions_frame,
    text="＋  Deposit",
    font=("Arial", 12, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=NAVY,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=18
)

deposit_button.pack(side="left", padx=(0, 15))

# =====================================
# START APPLICATION
# =====================================

root.mainloop()
