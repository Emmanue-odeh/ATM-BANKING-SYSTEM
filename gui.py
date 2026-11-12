
import tkinter as tk

# ==========================================
# SMART ATM - PREMIUM DARK BANKING DASHBOARD
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


# ==========================================
# MAIN WINDOW STRUCTURE
# ==========================================

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


# ==========================================
# LEFT SIDEBAR
# ==========================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=215
)

sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)


# ==========================================
# MAIN CONTENT AREA
# ==========================================

main_area = tk.Frame(
    root,
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



# ==========================================
# TOP DASHBOARD HEADER
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


# Dashboard welcome heading
welcome_label = tk.Label(
    header,
    text="Dashboard Overview",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=WHITE
)

welcome_label.grid(
    row=0,
    column=0,
    sticky="w"
)


# Dashboard subtitle
subtitle = tk.Label(
    header,
    text="Monitor your finances and banking activities",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
)

subtitle.grid(
    row=1,
    column=0,
    sticky="w",
    pady=(5, 0)
)


brand = tk.Label(
    sidebar,
    text="◆  SMART ATM",
    font=("Arial", 17, "bold"),
    bg=SIDEBAR,
    fg=WHITE
)

brand.pack(anchor="w", padx=20, pady=(25, 30))


# ==========================================
# CUSTOMER PROFILE CARD
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
# SIDEBAR MENU HEADING
# ==========================================

menu_heading = tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 8, "bold"),
    bg=SIDEBAR,
    fg=MUTED
)

menu_heading.pack(anchor="w", padx=20, pady=(30, 12))

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

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


for icon, title in navigation_items:
    create_navigation_button(icon, title)

# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()
