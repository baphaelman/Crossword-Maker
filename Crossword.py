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
        original_board = self.board.clone()

        important_words_generator = self.insert_important_words(important_words)
        while True:
            try:
                self.board = next(important_words_generator)
                self.board.words = important_words
            except StopIteration:
                break
            filled_board =  self.board.fill_board(size)
            if filled_board:
                self.board = filled_board
                break
            else:
                self.board = original_board.clone()
    
    def insert_important_words(self, words_list):
        if len(words_list) == 1:
            yield from self.board.generate_board(words_list[0])
        else:
            word = words_list[0]
            generator = self.board.generate_board(word)
            original = self.board.clone()
            while True:
                try:
                    self.board = next(generator)
                    yield from self.insert_important_words(words_list[1:])
                    self.board = original
                except StopIteration:
                    break
    
    def __repr__(self):
        rowString = ""
        for row in self.board.rows:
            for item in row:
                rowString += item
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
    # b = Crossword(3, ["can", "age"])
    c = Crossword(4, ["eats", "ants"])
    # print(b)
    print(c)

if __name__ == "__main__":
    # main()
    # broken_line_test()
    init_test()