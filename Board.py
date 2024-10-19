class Board:
    # self.board: list of lists representing the board (columns of rows)
    # self.cols: list of strings representing columns [ "happy", "j00k", ]
    # self.rows: list of strings representing rows
    def __init__(self, size):

        # initialize board with # along border, 0 in the center
        self.board = [] # list of columns, which are lists of row elements
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
        
        # initialize cols
        self.cols = []

        for _ in range(1, size - 1):
           word = ""
           word.append()

    def __init__(self, size, cols, rows):
        self.cols = cols
        self.rows = rows
        self.size = size
        self.board

    def get(self, row: int, col: int):
        return self.board[col][row]