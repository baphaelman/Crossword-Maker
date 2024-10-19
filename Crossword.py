from typing import List
from Board import Board

class Crossword:
    # self.size: size of crossword (ex. 5 -> 5x5)
    # self.board: instance of Board
    # self.words: list of words the user wants to include in the 

    def __init__(self, size: int, words: List[str]):
        self.size = size
        self.words = words

        self.board = Board(size)
    
    def __repr__(self):
        rowString = ""
        for row in self.board:
            for item in row:
                rowString += str(item)
                rowString += " "
            rowString += "\n"
            
        return rowString
    
    def valid_board(self):
        return self.valid_rows() and self.valid_columns()