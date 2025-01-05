import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.configure(bg="white")

# Game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Functions to handle the game logic
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def is_draw():
    for row in board:
        if "" in row:
            return False
    return True

def handle_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        buttons[row][col]["fg"] = "black" if current_player == "X" else "gray"

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Create the UI
title_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 20), bg="white", fg="black")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        button = tk.Button(
            frame,
            text="",
            font=("Helvetica", 24),
            width=5,
            height=2,
            bg="white",
            fg="black",
            command=lambda r=row, c=col: handle_click(r, c),
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons[row][col] = button

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), bg="white", fg="black", command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
