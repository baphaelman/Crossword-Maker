import tkinter as tk
from tkinter import messagebox
from Crossword import Crossword

class CrosswordGUI:

    def __init__(self, master):
        self.master = master
        master.title("Crossword Generator")

        # Create labels and entry fields
        self.size_label = tk.Label(master, text="Enter size of the crossword (e.g., 5):")
        self.size_label.pack()

        self.size_entry = tk.Entry(master)
        self.size_entry.pack()

        self.words_label = tk.Label(master, text="Enter your desired words separated by spaces:")
        self.words_label.pack()

        self.words_entry = tk.Entry(master)
        self.words_entry.pack()

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Crossword", command=self.generate_crossword)
        self.generate_button.pack()

        # Text area to display the crossword
        self.crossword_text = tk.Text(master, height=20, width=50)
        self.crossword_text.pack()

        # Buttons to accept or generate another crossword
        self.accept_button = tk.Button(master, text="Accept Crossword", command=self.accept_crossword, state=tk.DISABLED)
        self.accept_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.another_button = tk.Button(master, text="Generate Another Crossword", command=self.generate_another, state=tk.DISABLED)
        self.another_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Initialize variables
        self.crossword = None
        self.important_words_generator = None
        self.filled_board_generator = None

    def generate_crossword(self):
        size_text = self.size_entry.get()
        words_text = self.words_entry.get()

        if not size_text.isdigit():
            messagebox.showerror("Invalid input", "Size must be an integer")
            return

        size = int(size_text)
        important_words = words_text.strip().split()

        # Clear the crossword text area
        self.crossword_text.delete(1.0, tk.END)

        # Initialize crossword
        try:
            self.crossword = Crossword(size, important_words)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        # Generate crossword
        self.important_words_generator = self.crossword.insert_important_words(important_words)
        self.generate_next_crossword()

    def generate_next_crossword(self):
        while True:
            try:
                self.crossword.board = next(self.important_words_generator)
                self.crossword.board.words = self.crossword.important_words
            except StopIteration:
                messagebox.showinfo("No more crosswords", "There are no valid crosswords with these words! Please try others")
                self.accept_button.config(state=tk.DISABLED)
                self.another_button.config(state=tk.DISABLED)
                return

            # Try filling board
            self.filled_board_generator = self.crossword.board.fill_board(self.crossword.size)
            try:
                self.crossword.board = next(self.filled_board_generator)
            except StopIteration:
                continue

            # Display crossword
            self.crossword_text.delete(1.0, tk.END)
            self.crossword_text.insert(tk.END, str(self.crossword))
            self.accept_button.config(state=tk.NORMAL)
            self.another_button.config(state=tk.NORMAL)
            break

    def accept_crossword(self):
        messagebox.showinfo("Crossword Accepted", "Happy crosswording!")
        self.accept_button.config(state=tk.DISABLED)
        self.another_button.config(state=tk.DISABLED)

    def generate_another(self):
        try:
            self.crossword.board = next(self.filled_board_generator)
            self.crossword_text.delete(1.0, tk.END)
            self.crossword_text.insert(tk.END, str(self.crossword))
        except StopIteration:
            # No more crosswords with current important words, try next important words board
            self.generate_next_crossword()

if __name__ == "__main__":
    root = tk.Tk()
    gui = CrosswordGUI(root)
    root.mainloop()
