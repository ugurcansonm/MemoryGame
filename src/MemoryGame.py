import tkinter as tk
import random
from tkinter import messagebox

# --- GAME CONFIGURATION ---
ROWS, COLS = 4, 4

attempts = 0
found_pairs = 0
open_cards = []
matched_indices = []
is_locked = False 
card_values = []
buttons = []

root = tk.Tk()

# --- ASSET LOADING AND SCALING ---
SCALE_FACTOR = 2

def load_and_scale(file_path):
    """Loads and scales images by the global factor."""
    img = tk.PhotoImage(file=file_path)
    return img.subsample(SCALE_FACTOR, SCALE_FACTOR)

# NOTE: Update this path according to your local environment (e.g., "./assets")
BASE_PATH = "C:/Users/<YOUR_USERNAME>/Desktop/Assets"

back_img = load_and_scale(f"{BASE_PATH}/back.png")
app_icon = tk.PhotoImage(file=f"{BASE_PATH}/card.png") 

card_images = {}
for i in range(1, 9):
    card_images[i] = load_and_scale(f"{BASE_PATH}/rc{i}.png")

root.iconphoto(False, app_icon)
root.resizable(False, False)

# --- GAME MECHANICS ---

def start_game():
    global attempts, found_pairs, open_cards, matched_indices, is_locked, card_values
    attempts = 0
    found_pairs = 0
    open_cards = []
    matched_indices = []
    is_locked = False
    
    card_values = list(range(1, 9)) * 2
    random.shuffle(card_values)
    
    # Reset all buttons to the default back image
    for btn in buttons:
        btn.config(image=back_img)
    
    update_title()

def update_title():
    root.title(f"Memory Game - Attempts: {attempts} | Pairs Found: {found_pairs}/8")

def on_card_click(k):
    global attempts, found_pairs, open_cards, is_locked
    
    # Prevent interacting with locked, already matched, or already opened cards
    if is_locked or k in matched_indices or k in open_cards:
        return
    
    card_id = card_values[k]
    buttons[k].config(image=card_images[card_id])
    open_cards.append(k)
    
    if len(open_cards) == 2:
        is_locked = True 
        attempts += 1
        update_title()
        root.after(600, check_match)

def check_match():
    global found_pairs, open_cards, matched_indices, is_locked
    
    idx1, idx2 = open_cards
    if card_values[idx1] == card_values[idx2]:
        found_pairs += 1
        matched_indices.extend([idx1, idx2])
    else:
        buttons[idx1].config(image=back_img)
        buttons[idx2].config(image=back_img)
    
    open_cards = []
    is_locked = False 
    update_title()
    
    if found_pairs == 8:
        if messagebox.askyesno("Game Over", "Congratulations! You found all pairs. Do you want to exit?"):
            root.destroy()
        else:
            start_game()

# --- INTERFACE GENERATION ---
main_frame = tk.Frame(root)
main_frame.pack(padx=5, pady=5)

for i in range(16):
    btn = tk.Button(
        main_frame, 
        image=back_img, 
        bd=1, 
        relief='ridge', 
        command=lambda k=i: on_card_click(k)
    )
    btn.grid(row=i // 4, column=i % 4, padx=2, pady=2)
    buttons.append(btn)

start_game()
root.mainloop()