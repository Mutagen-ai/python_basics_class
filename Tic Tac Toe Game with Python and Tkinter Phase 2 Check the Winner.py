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

# ================================================
# PHASE 2: CHECK THE WINNER
# ================================================

def check_winner():
    # all 8 possible winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]                # diagonals
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]   # return the winning player
    return None               # no winner yet


def click(index):
    global current_player

    # ignore click if the square is already taken
    if board[index] != "":
        return

    # place the current player's mark on the board
    board[index] = current_player

    # check if this move made someone win
    winner = check_winner()

    if winner:
        scores[winner] += 1
        score_label.config(text=f"X: {scores['X']}   O: {scores['O']}")
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset()
        return

    # check if the board is full with no winner, meaning a draw
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset()
        return

    # switch turns to the other player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    status_label.config(text=f"Player {current_player}'s turn")


def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status_label.config(text="Player X's turn")


# start the window
window.mainloop()