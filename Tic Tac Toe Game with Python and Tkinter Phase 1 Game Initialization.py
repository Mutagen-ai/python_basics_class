import tkinter as tk
from tkinter import messagebox

# ================================================
# PHASE 1: GAME INITIALIZATION
# ================================================

# the board is a list of 9 empty strings
# each index represents a square on the board
# 0 1 2
# 3 4 5
# 6 7 8
board = [""] * 9

# X always goes first
current_player = "X"

# keep track of how many times each player has won
scores = {"X": 0, "O": 0}

# main window setup
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# title label at the top of the window
tk.Label(window, text="Tic Tac Toe", font=("Arial", 18, "bold")).pack(pady=10)

# score label
score_label = tk.Label(window, text="X: 0   O: 0", font=("Arial", 13))
score_label.pack()

# status label to show whose turn it is
status_label = tk.Label(window, text="Player X's turn", font=("Arial", 12))
status_label.pack(pady=5)

# start the window
window.mainloop()