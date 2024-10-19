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
    
    

def main():
    b = Crossword(3, [])
    # print(b.board)
    # b.board.insert_char("f" , 2, 3)
    # print(b.board)
    generator = b.board.generate_board("can")
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    

if __name__ == "__main__":
    main()





