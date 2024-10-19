class Board:
    # self.board: list of lists representing the board (columns of rows)
    # self.cols: list of strings representing columns [ "happy", "j00k", ]
    # self.rows: list of strings representing rows
    # self.size: size of inner board
    # self.true_size: size of board, including border

    def __init__(self, size, cols=None, rows=None):
        self.size = size
        self.true_size = size + 2
        if cols and rows: # inputting existing board
            self.cols = cols
            self.rows = rows
            
            self.board = []
            for i in range(self.true_size):
                col_builder = []
                for j in range(self.true_size):
                    if i == 0 or i == self.true_size - 1:
                        col_builder.append("#")
                    elif j == 0 or j == self.true_size - 1:
                        col_builder.append("#")
                    else:
                        word = self.rows[j - 1]
                        char = word[i - 1]
                        col_builder.append(char)
                self.board.append(col_builder)
        else: # initializing new board
            # initialize cols
            self.cols = []

            word = ""
            for _ in range(1, size + 1):
                word += "0"
            
            for _ in range(1, size + 1):
                self.cols.append(word)
            
            # initialize rows
            self.rows = list(self.cols)

            # initialize board with # along border, 0 in the center
            self.board = []
            for col in range(size + 2):
                row_builder = []
                for row in range(size + 2):
                    if col == 0 or col == size + 1:
                        row_builder.append("#")
                    elif row == 0 or row == size + 1:
                        row_builder.append("#")
                    else:
                        row_builder.append(0)
                self.board.append(row_builder)
    
    
    # returns character at row and col
    def get(self, row: int, col: int):
        return self.board[col][row]
    
    def __repr__(self):
        rowString = ""
        for  i in range(self.true_size):
            for j in range(self.true_size):
                rowString += str(self.get(i, j))
                rowString += " "
            rowString += "\n"
            
        return rowString

def main():
    cols = ["abc", "def", "ghi"]
    rows = ["adg", "beh", "cfi"]
    b = Board(3, cols, rows)
    print(b)

if __name__ == "__main__":
    b = Board(3)
    print(b)
    main()