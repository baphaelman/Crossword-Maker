class Crossword:
    def __init__(self, size):
        self.size = size
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
