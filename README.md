# MemoryGame

A lightweight, interactive, and grid-based 2D Memory (Card Matching) game built using Python and the Tkinter GUI toolkit. The application features dynamic asset scaling, asynchronous move validation, and status tracking to provide a polished desktop gaming experience.

---

## 🚀 Features

* **Dynamic Grid System:** Generates a randomized $4\times4$ layout housing 8 unique pairs of hidden cards.
* **Asynchronous Matching Logic:** Implements a timed latch system (`root.after`) that pauses the board for 600ms upon flipping two cards, allowing players to briefly memorize non-matching pairs before they flip back.
* **State & Interaction Protection:** Utilizes an interaction lock (`is_locked`) preventing illegal inputs (e.g., multi-clicking during checks or re-clicking already opened/matched pairs).
* **Live Score & Metric Tracking:** Real-time update of player attempts and found pairs reflected directly inside the application's native title window.
* **Robust Session Management:** Prompts the user with a customized choice box at game completion to either gracefully exit or reset the environment instantly for a new run.

---

## 🛠️ Project Structure

To maintain a clean and professional architecture, it is recommended to organize your local directory as follows:

<img width="649" height="848" alt="MemoryGame" src="https://github.com/user-attachments/assets/1e2ba3ca-1116-4bd4-a9ea-6f79e2def925" />

```text
Memory-Game/
├── assets/
│   ├── back.png                 # Default card back texture
│   ├── card.png                 # Window application icon
│   ├── rc1.png ... rc8.png      # 8 unique card front textures
│   └── MemoryGame.png  # Preview image for repository documentation
├── src/
│   └── MemoryGame.py                  # Primary Python implementation source code
├── .gitignore
└── README.md                    # Project landing page documentation
