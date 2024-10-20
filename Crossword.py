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

        for important_word in important_words:
            generator = self.board.generate_board(important_word)
            try:
                while True:
                    self.board = next(generator)
            except StopIteration:
                pass
    
    def __repr__(self):
        rowString = ""
        for row in self.board.rows:
            for item in row:
                rowString += str(item)
                rowString += " "
            rowString += "\n"
            
        return rowString
    
    

def main():
    b = Crossword(3, [])
    b.board.insert_char("f" , 1, 2)
    generator = b.board.generate_board("can")
    for i in generator:
        print(i)

def broken_line_test():
    b = Crossword(4, [])
    b.board.insert_char("#", 1, 1)
    generator = b.board.generate_board("can")
    for i in generator:
        print(i)

def init_test():
    b = Crossword(3, ["can", "age"])
    print(b)

if __name__ == "__main__":
    # main()
    # broken_line_test()
    init_test()