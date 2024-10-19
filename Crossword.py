from typing import List
from Board import Board

class Crossword:
    # self.size: size of crossword (ex. 5 -> 5x5)
    # self.board: instance of Board
    # self.important_words: list of important_words the user wants to include in the 

    def __init__(self, size: int, important_words: List[str]):
        self.size = size
        self.important_words = important_words

        self.board = Board(size)
    
    def __repr__(self):
        rowString = ""
        for row in self.board:
            for item in row:
                rowString += str(item)
                rowString += " "
            rowString += "\n"
            
        return rowString
    
    def generate_board(self, word):
        board = self.board
        #word is down
        for i in range (1, len(board.cols) + 1):
            for j in range (1, len(board.rows) - len(word)):
                valid = True
                for k in range (0, len(word)):
                    if (board.get(j + k,i)) != word[k] and board.get(j + k, i) != "0":
                        valid = False
                if valid:
                    new_board = board.clone()
                    for k in range (0, len(word)):
                        new_board.insert(j + k, i , word[k])
                        if new_board.valid_board():
                            yield new_board
                        
        #word is across
        for i in range (1, len(board.rows)):
            for j in range (1, len(board.cols) - len(word)):
                valid = True
                for k in range (0, len(word)):
                    if (board.get(i, j + k)) != word[k] and board.get(i, j + k) != 0:
                        valid = False
                if valid:
                    new_board = board.clone()
                    for k in range (0, len(word)):
                        new_board.insert(i,  j + k , word[k])
                        if new_board.valid_board():
                            yield new_board

def main():
    b = Crossword(3, [])
    generator = b.generate_board("can")
    print(next(generator))

if __name__ == "__main__":
    main()





