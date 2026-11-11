import tkinter as tk

root  = tk.Tk()

root.title("SMART ATM")
root.geometry("900x600")
root.configure(bg="#f2f5f9")

title_label = tk.Label(
    root,
    text="SMART ATM",
    font=("Arial", 26, "bold"),
    bg="#f2f5f9",
    fg="#14213d"
)

title_label.pack(pady=40)

root.mainloop()