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
    # self.words: list of words added to the board

    # INSTANCE METHODS
    # get(row, col) -> str: returns the entry at row and col indices
    # is_valid() -> bool: returns whether the partially-completed board is valid, considering common_words
    # insert(char, row, col) -> None: inserts char at row and col indices
    # clone() -> Board: returns a copy of the board
    # transpose() -> Board: returns a transposed copy of the board

    def __init__(self, size, cols=None, rows=None, board=None):
        self.size = size
        self.words = []
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
            
            self.cols = [word for _ in range(size)]

            # initialize rows
            self.rows = list(self.cols)

            # initialize board with # along border, 0 in the center
            self.board = [['0' for _ in range(size)] for _ in range(size)]
    
    
    # returns character at row and col
    def get(self, row: int, col: int):
        return self.board[col][row]
    
    def __repr__(self):
        rowString = ""
        for i in range(self.size):
            for j in range(self.size):
                rowString += str(self.get(i, j))
                rowString += " "
            if (i < self.size - 1):
                rowString += "\n"
        
        return rowString
    
    # returns whether the partially completed board is valid, using words from common_words and lists rows_ and cols_indeces
    def is_valid(self, rows_indeces, cols_indeces):
        transpose = self.transpose()
        return self.is_valid_cols(cols_indeces) and transpose.is_valid_cols(rows_indeces)
    
    def is_valid_cols(self, cols_indeces):
        col_words = []
        for i in cols_indeces:
            word = self.cols[i]
            col_words.extend(word.split("#"))
        
        # checks if each word is potentially valid
        original = [common_word for common_word in common_words if len(common_word) == len(word)]
        valid_words = list(original)
        for word in col_words:
            for i in range(len(word)):
                char = word[i]
                if char != "0":
                    valid_words = [word for word in valid_words if word[i] == char]
                    if not valid_words:
                        return False
            valid_words = list(original)
        return True
    
    def is_filled(self) -> bool:
        for word in self.cols:
            for letter in word:
                if letter == "0":
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
        return Board(self.size, new_cols, list(self.rows), new_board)
    
    # returns a transposed copy of the board
    def transpose(self) -> 'Board':
        new_cols = list(self.cols)
        new_board = []
        for row in range(self.size):
            column_list = []
            for col in range(self.size):
                column_list.append(new_cols[col][row])
            new_board.append(list(column_list))
        return Board(self.size, list(self.rows), new_cols, new_board)
    
    def generate_board(self, word):
        board = self
    
        #word is down
        for col in range (0, len(board.cols)):
            for j in range (0, len(board.rows) - len(word) + 1):
                valid = True
                for k in range (0, len(word)):
                    if (board.get(j + k, col)) != word[k] and board.get(j + k, col) != "0":
                        valid = False
                if valid:
                    new_board = board.clone()
                    for k in range (0, len(word)):
                        new_board.insert_char(word[k], j + k, col)
                    if new_board.is_valid(range(self.size), [col]):
                        yield new_board
                        
        #word is across
        for i in range (0, len(board.rows)):
            for j in range (0, len(board.cols) - len(word) + 1):
                valid = True
                for k in range (0, len(word)):
                    if (board.get(i, j + k)) != word[k] and board.get(i , j + k) != "0":
                        valid = False
                if valid:
                    new_board = board.clone()
                    for k in range (0, len(word)):
                        new_board.insert_char(word[k], i,  j + k)
                        
                    if new_board.is_valid([i], range(self.size)):
                        yield new_board

    def fill_board(self, row):
        row_index = row - 1
        row_word = self.rows[row_index]

        # filtering common_words
        potential_words = [word for word in common_words if len(word) == self.size and word not in self.words]
        for i in range(len(row_word)):
            potential_words = [word for word in potential_words if row_word[i] == '0' or word[i] == row_word[i]]
        
        original = self.clone()
        if row_index == 0:
            for potential_word in potential_words:
                self.insert_word(potential_word, 0, 0, Board.ROW)
                if self.is_valid([row_index], range(self.size)): # FIX THIS
                    if not self.is_filled():
                        self = original.clone()
                    else:
                        yield self
                else:
                    self = original.clone()
            return
        else:
            for potential_word in potential_words:
                self.insert_word(potential_word, row_index, 0, Board.ROW)
                if self.is_valid([row_index], range(self.size)): # FIX THIS
                    yield from self.fill_board(row - 1)
                self = original.clone()
       

def main():
    cols = ["abc", "d#f", "ghi"]
    rows = ["adg", "beh", "cfi"]
    b = Board(3, cols, rows)
    print(b)

def is_valid_test():
    bad_cols = ["car", "ago", "0qz"]
    bad_rows = ["ca0", "agq", "roz"]
    bad_b = Board(3, bad_cols, bad_rows)
    print('expected True: ', bad_b.is_valid([0], [0, 1]))
    print('expected False: ', bad_b.is_valid([0, 1], [0, 1]))
    print('expected False: ', bad_b.is_valid([0, 1, 2], [0, 1, 2]))

    cols = ["car", "ago", "new"]
    rows = ["can", "age", "row"]
    b = Board(3, cols, rows)
    print('expected True: ', b.is_valid([0, 1, 2], [0, 1, 2]))

    c = Board(3)
    print('expected True: ', c.is_valid([2], [1]))

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

def is_filled_test():
    b = Board(3)
    print("expecting False: ", b.is_filled())

    cols = ["c00", "a00", "n00"]
    rows = ["can", "000", "000"]
    # c a n
    # 0 0 0
    # 0 0 0
    c = Board(3, cols, rows)
    print('expecting False: ', c.is_filled())

    cols = ["abc", "d#f", "ghi"]
    rows = ["adg", "beh", "cfi"]
    d = Board(3, cols, rows)
    print("expecting True:", d.is_filled())

def transpose_test():
    cols = ["car", "ago", "new"]
    rows = ["can", "age", "row"]
    b = Board(3, cols, rows)
    print(b)

    trans = b.transpose()
    print(trans)

if __name__ == "__main__":
    is_valid_test()