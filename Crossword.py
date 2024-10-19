class Crossword:
    def __init__(self, size):
        self.size = size
        self.board = []
        for col in range(size + 2):
            row_builder = []
            for row in range(size + 2):
                if row == 0 or row == size + 1:
                    row_builder.append("#")
                elif col == 0 or col == size + 1:
                    row_builder.append("#")
                row_builder.append(None)
            self.board.append(row_builder)
        print(self.board)