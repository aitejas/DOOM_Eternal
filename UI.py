import tkinter as tk
import subprocess
import sys

# ------------------ FUNCTIONS ------------------

def start_game():
    root.destroy()
    subprocess.Popen([sys.executable, "main.py"])

def open_leaderboard():
    print("Leaderboard Opened")

def how_to_play():
    print("How to Play Opened")

def open_settings():
    print("Settings Opened")

# ------------------ MAIN WINDOW ------------------

root = tk.Tk()
root.title("Game UI")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#2b0b4f")

# ------------------ TITLE ------------------

title = tk.Label(
    root,
    text="GAME",
    font=("Arial", 64, "bold"),
    fg="#ff4fd8",
    bg="#2b0b4f"
)
title.pack(pady=(80, 10))

subtitle = tk.Label(
    root,
    text="Ready to play?",
    font=("Arial", 18),
    fg="white",
    bg="#2b0b4f"
)
subtitle.pack(pady=(0, 30))

# ------------------ BUTTON STYLE ------------------

def create_button(text, command):
    return tk.Button(
        root,
        text=text,
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#a020f0",
        activebackground="#ff1493",
        activeforeground="white",
        relief="flat",
        bd=0,
        width=20,
        height=2,
        command=command
    )

# ------------------ BUTTONS ------------------

start_btn = create_button("▶  Start Game", start_game)
start_btn.pack(pady=10)

leaderboard_btn = create_button("🏆  Leaderboard", open_leaderboard)
leaderboard_btn.pack(pady=10)

bottom_frame = tk.Frame(root, bg="#2b0b4f")
bottom_frame.pack(pady=20)

how_btn = create_button("❓  How to Play", how_to_play)
how_btn.grid(in_=bottom_frame, row=0, column=0, padx=20)

settings_btn = create_button("⚙  Settings", open_settings)
settings_btn.grid(in_=bottom_frame, row=0, column=1, padx=20)

footer = tk.Label(
    root,
    text="Press Start to begin your adventure",
    font=("Arial", 10),
    fg="lightgray",
    bg="#2b0b4f"
)
footer.pack(pady=40)

root.mainloop()