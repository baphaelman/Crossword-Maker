from parser import common_words

class Board:
    # STATIC VARIABLES
    # board.ROW: represents row direction
    # board.COLUMN: you can figure this one out bro
    ROW = True
    COLUMN = False

    # INSTANCE VARIABLES
    # self.board: list of lists representing the board (columns of rows)
    # self.cols: list of strings representing columns ["happy", "j00ky", ...]
    # self.rows: list of strings representing rows
    # self.size: nxn size of board

    # INSTANCE METHODS
    # get(row, col) -> str: returns the entry at row and col indices
    # valid_board() -> bool: returns whether the partially-completed board is valid, considering common_words
    # insert(char, row, col) -> None: inserts char at row and col indices
    # clone() -> Board: returns a copy of the board
    # transpose() -> Board: returns a transposed copy of the board

    def __init__(self, size, cols=None, rows=None, board=None):
        self.size = size
        if cols and rows: # inputting existing board
            self.cols = cols
            self.rows = rows
            
            if board:
                self.board = board
            else:
                self.board = []
                for col in range(size):
                    column_list = []
                    for row in range(size):
                        column_list.append(cols[col][row])
                    self.board.append(list(column_list))
        else: # initializing new board
            # initialize cols
            self.cols = []

            word = ""
            for _ in range(size):
                word += "0"
            
            for _ in range(1, size + 1):
                self.cols.append(word)

            # initialize rows
            self.rows = list(self.cols)

            # initialize board with # along border, 0 in the center
            self.board = []
            row_builder = []
            for _ in range(size):
                row_builder.append("0")
            
            for _ in range(size):
                self.board.append(list(row_builder))
    
    
    # returns character at row and col
    def get(self, row: int, col: int):
        return self.board[col][row]
    
    def __repr__(self):
        rowString = ""
        for  i in range(self.size):
            for j in range(self.size):
                rowString += str(self.get(i, j))
                rowString += " "
            rowString += "\n"
            
        return rowString
    
    # returns whether the partially completed board is valid, using words from common_words
    def valid_board(self) -> bool:
        transpose = self.transpose()
        return self.valid_cols() and transpose.valid_cols()

    def valid_cols(self):
        # splits self.cols into each word
        col_words = []
        for word in self.cols:
            col_words.extend(word.split("#"))
        
        # checks if each word is potentially valid
        for word in col_words:
            valid_words = [common_word for common_word in common_words if len(common_word) == len(word)]
            for i in range(len(word)):
                char = word[i]
                if char != "0":
                    valid_words = [word for word in valid_words if word[i] == char]
                    if not valid_words:
                        return False
        return True

    # inserts char at row and col index
    def insert_char(self, char: str, row: int, col: int) -> None:
        self.board[col][row] = char

        col_word = self.cols[col]
        self.cols[col] = col_word[:row] + char + col_word[row + 1:]

        row_word = self.rows[row]
        self.rows[row] = row_word[:col] + char + row_word[col + 1:]
    
    def insert_word(self, word: str, row: int, col: int, direction: bool) -> None:
        if not direction:
            row_change = 1
            col_change = 0
        else:
            row_change = 0
            col_change = 1

        for char in word:
            self.insert_char(char, row, col)
            row += row_change
            col += col_change
    
    # returns a copy of the board
    def clone(self) -> 'Board':
        new_cols = list(self.cols)
        new_board = []
        for col in range(self.size):
            column_list = []
            for row in range(self.size):
                column_list.append(new_cols[col][row])
            new_board.append(list(column_list))
        return Board(self.size, list(self.cols), list(self.rows), new_board)
    
    # returns a transposed copy of the board
    def transpose(self) -> 'Board':
        return Board(self.size, list(self.rows), list(self.cols), list(self.board))

def main():
    cols = ["abc", "d#f", "ghi"]
    rows = ["adg", "beh", "cfi"]
    b = Board(3, cols, rows)
    print(b)
    b.valid_cols()
    print(b.cols)

def valid_test():
    bad_cols = ["car", "ago", "0qz"]
    bad_rows = ["ca0", "agq", "roz"]
    bad_b = Board(3, bad_cols, bad_rows)
    print(bad_b.valid_board())

    cols = ["car", "ago", "new"]
    rows = ["can", "age", "row"]
    b = Board(3, cols, rows)
    print(b.valid_board())

    c = Board(3)
    print(c.valid_board())

def valid_test2():
    cols = ["car", "ago", "new"]
    rows = ["can", "age", "row"]
    b = Board(3, cols, rows)
    print(b.valid_board())

def insert_test():
    cols = ["c00", "a00", "n00"]
    rows = ["can", "000", "000"]
    # c a n
    # 0 0 0
    # 0 0 0
    b = Board(3, cols, rows)
    b.insert_word("age", 0, 1, Board.COLUMN)
    b.insert_word("ago", 1, 0, Board.ROW)
    print(b)

def insert_char_test():
    b = Board(3)
    b.insert_char("a", 1, 1)
    print(b)


if __name__ == "__main__":
    valid_test()
    valid_test2()