import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Tic Tac Toe")

        self.mode = None  # "one" or "two"
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.choose_mode()

    def choose_mode(self):
        def set_mode_one():
            self.mode = "one"
            mode_win.destroy()
            self.create_widgets()

        def set_mode_two():
            self.mode = "two"
            mode_win.destroy()
            self.create_widgets()

        mode_win = tk.Toplevel(self.root)
        mode_win.title("Choose Mode")
        tk.Label(mode_win, text="Choose Game Mode:", font=("Helvetica", 14)).pack(padx=20, pady=10)

        tk.Button(mode_win, text="One Player (vs Computer)", font=("Helvetica", 12), width=25, command=set_mode_one).pack(pady=5)
        tk.Button(mode_win, text="Two Players", font=("Helvetica", 12), width=25, command=set_mode_two).pack(pady=5)

        mode_win.transient(self.root)
        mode_win.grab_set()
        self.root.wait_window(mode_win)

    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Helvetica', 32), height=2, width=5,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, i):
        if self.buttons[i]["text"] == "" and not self.check_winner():
            self.make_move(i, self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"🏆 Player {self.current_player} wins!")
                self.ask_restart()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "🤝 It's a tie!")
                self.ask_restart()
            else:
                self.switch_player()

                if self.mode == "one" and self.current_player == "O":
                    self.root.after(500, self.computer_move)  # delay for better UX

    def make_move(self, index, player):
        self.buttons[index]["text"] = player
        self.board[index] = player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                  (0, 4, 8), (2, 4, 6)]             # diagonals
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def computer_move(self):
        empty_cells = [i for i, val in enumerate(self.board) if val == ""]
        if empty_cells:
            move = random.choice(empty_cells)
            self.make_move(move, "O")

            if self.check_winner():
                messagebox.showinfo("Game Over", f"💻 Computer (O) wins!")
                self.ask_restart()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "🤝 It's a tie!")
                self.ask_restart()
            else:
                self.switch_player()

    def ask_restart(self):
        if messagebox.askyesno("Restart", "Do you want to play again?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
