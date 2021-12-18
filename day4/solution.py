# Challenge 1
class BingoBoard:
    def __init__(self):
        self.position = {}
        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0]
        }

    def initialize(self, row, numbers):
        index = 0
        for i in range(5):
            self.board[i][row] = numbers[i]
            index += 1
            if index == 24:
                break

    def fillBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def isBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]

    def update(self, val):
        x, y = self.position[val]
        self.board[x][y] = 'X'
        self.fillBingo(x, y)

    def __str__(self):
        return board


with open("input.txt") as file:
    content = file.read().splitlines()

drawings = content[0]
boards = []

board = BingoBoard()
row = 0
for i in range(1, len(content)):
    if row != 0 and row % 5 == 0:
        boards.append(board)
        board = BingoBoard()
        row = 0
    if content[i] == '':
        i += 1
    else:
        board.initialize(row, [int(l) for l in content[i].split()])
        row += 1

print(drawings)
