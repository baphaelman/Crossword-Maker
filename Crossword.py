from typing import List
from Board import Board
from parser import common_words

class Crossword:
    # self.size: size of crossword (ex. 5 -> 5x5)
    # self.board: instance of Board
    # self.important_words: list of important_words the user wants to include in the

    def __init__(self, size: int, important_words: List[str]):
        self.size = size
        self.important_words = important_words

        # initialize common_words list
        self.common_words = common_words[size]
        self.common_words.extend(important_words)

        self.board = Board(size, common_words=self.common_words)
    
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
        return self.board.__repr__()
    
    

def main():
    size = int(input("Enter the size of the crossword: "))
    
    while True:
        # try generating feasible important_words board
        try:
            words_input = input("Enter your desired words separated by spaces: ")
            important_words = words_input.split()

            crossword = Crossword(size, important_words)

            important_words_generator = crossword.insert_important_words(important_words)
            crossword.board = next(important_words_generator)
            crossword.board.words = important_words
        except StopIteration:
            print("There are no valid crosswords with these words! Please try others")
            continue
        while True:
            # try filling board
            filled_board_generator = crossword.board.fill_board(size)
            while True:
                try:
                    crossword.board = next(filled_board_generator)
                except StopIteration:
                    break

                print(crossword)
                while True:
                    another_board = input("Are you satisfied with this board? (y/n) ")
                    print()
                    if another_board == "n":
                        try:
                            crossword.board = next(filled_board_generator)
                            print(crossword)
                            continue
                        except StopIteration:
                            break
                    elif another_board == "y":
                        print("Happy crosswording!")
                        return
                    else:
                        print("please enter a valid string: 'y' or 'n'")
                break
            print("Sorry, there are no other valid boards with these words")
            break

def broken_line_test():
    b = Crossword(4, [])
    b.board.insert_char("#", 1, 1)
    generator = b.board.generate_board("can")
    for i in generator:
        print(i)

def init_test():
    d = Crossword(4, ["scam", "tone"])

def init_test2():
    c = Crossword(4, ["gana", "girn"])

def init_test3():
    b = Crossword(3, ["can", "age"])

def init_test4():
    b = Crossword(4, ["eggs", "pain"])

def whats_common_words():
    b = Crossword(4, ["eggs", "pain"])
    print(type(b.common_words))
    print(b.common_words)

if __name__ == "__main__":
    main()