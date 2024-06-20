import tkinter as tk
from tkinter import font
from ai_tictactoe import is_winner, is_board_full, best_move, easy_move, medium_move

class TicTacToeGUI:
    def __init__(self, root):
        """
        Initialize the Tic Tac Toe GUI.

        Parameters:
        root (tk.Tk): The root window for the GUI.
        """
        self.root = root
        self.root.title("Tic Tac Toe")

        self.difficulty = tk.StringVar(value="Medium")
        
        # Create the difficulty selection buttons
        self.easy_button = tk.Radiobutton(root, text="Easy", variable=self.difficulty, value="Easy")
        self.medium_button = tk.Radiobutton(root, text="Medium", variable=self.difficulty, value="Medium")
        self.hard_button = tk.Radiobutton(root, text="Hard", variable=self.difficulty, value="Hard")
        
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.message_label = tk.Label(root, text="Select Difficulty", font=("Verdana", 16), fg="black")
        self.message_label.pack()
        
        # Pack difficulty buttons below the message label
        self.hard_button.pack(side=tk.BOTTOM)
        self.medium_button.pack(side=tk.BOTTOM)
        self.easy_button.pack(side=tk.BOTTOM)
        
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)

        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.move_count = 0

    def draw_board(self):
        """Draw the Tic Tac Toe board."""
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=5)
            self.canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=5)

    def draw_symbol(self, row, col):
        """
        Draw the symbol (X or O) on the board.

        Parameters:
        row (int): The row index.
        col (int): The column index.
        """
        x = col * 100 + 50
        y = row * 100 + 50

        if self.board[row][col] == "X":
            self.canvas.create_line(x - 25, y - 25, x + 25, y + 25, fill="blue", width=10)
            self.canvas.create_line(x + 25, y - 25, x - 25, y + 25, fill="blue", width=10)
        else:
            self.canvas.create_oval(x - 25, y - 25, x + 25, y + 25, outline="red", width=10)

    def on_click(self, event):
        """
        Handle a click event on the board.

        Parameters:
        event (tk.Event): The click event.
        """
        row = event.y // 100
        col = event.x // 100

        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.draw_symbol(row, col)
            self.move_count += 1

            if self.move_count == 1:
                self.disable_difficulty_buttons()

            if self.check_winner():
                self.display_winner(self.current_player)
            elif self.move_count == 9:
                self.display_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    if self.difficulty.get() == "Easy":
                        ai_row, ai_col = easy_move(self.board)
                    elif self.difficulty.get() == "Medium":
                        ai_row, ai_col = medium_move(self.board)
                    else:  # Hard
                        ai_row, ai_col = best_move(self.board)
                    
                    self.board[ai_row][ai_col] = "O"
                    self.draw_symbol(ai_row, ai_col)
                    self.move_count += 1
                    if self.check_winner():
                        self.display_winner("O")
                    elif self.move_count == 9:
                        self.display_draw()
                    else:
                        self.current_player = "X"

    def disable_difficulty_buttons(self):
        """Disable the difficulty selection buttons."""
        self.easy_button.config(state=tk.DISABLED)
        self.medium_button.config(state=tk.DISABLED)
        self.hard_button.config(state=tk.DISABLED)

    def check_winner(self):
        """
        Check if there is a winner.

        Returns:
        bool: True if there is a winner, False otherwise.
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def display_winner(self, winner):
        """
        Display the winner.

        Parameters:
        winner (str): The symbol of the winning player.
        """
        self.canvas.unbind("<Button-1>")
        message = f"Player {winner} wins!"
        self.message_label.config(text=message, fg="green")

    def display_draw(self):
        """Display a draw message."""
        self.canvas.unbind("<Button-1>")
        message = "It's a draw!"
        self.message_label.config(text=message, fg="orange")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
