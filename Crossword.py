from typing import List

class Crossword:
    # self.size: size of crossword (ex. 5 -> 5x5)
    # self.board: list of lists. size + 2 for hashtages along border
    # self.words: list of words the user wants to include in the 

    def __init__(self, size: int, words: List[str]):
        self.size = size
        self.words = words

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
        print(self.board)
    
    def __repr__(self):
        rowString = ""
        for row in self.board:
            for item in row:
                rowString += str(item)
                rowString += " "
            rowString += "\n"
            
        return(rowString)
