# User Interface for Rock-Paper-Scissors

from tkinter import Tk, Label, Button, ttk
from game_logic import spin

# Create Object
root = Tk()

# Set geometry
root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

# Function to update the UI based on the game result
def update_ui():
    user_choice = user_select.get()
    result = spin(user_choice)
    wl_label.config(text=result)

# Adding dropdown box for Rock, Paper, Scissors
user_select = ttk.Combobox(root, value=["Rock", "Paper", "Scissors"])
user_select.current(0)
user_select.pack()

# Add Labels, Button
wl_label = Label(root, text="", font=("arial", 10), width=50, height=4)
wl_label.pack()

button = Button(root, text="Spin!", font=("bell mt", 10), command=update_ui)
button.pack()

root.mainloop()