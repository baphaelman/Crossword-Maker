from parser import common_words

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
    
    # returns whether the partially completed board is valid, using words from common_words
    def valid_board(self):
        return self.valid_cols() and self.transpose().cols()
    
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

def main():
    cols = ["abc", "d#f", "ghi"]
    rows = ["adg", "beh", "cfi"]
    b = Board(3, cols, rows)
    print(b)
    b.valid_cols()
    print(b.cols)

def valid_test():
    cols = ["car", "ago", "0qz"]
    rows = ["caq", "age", "row"]
    b = Board(3, cols, rows)
    for word in cols:
        print(f"word: {word}")
    print(b.valid_cols())

if __name__ == "__main__":
    valid_test()