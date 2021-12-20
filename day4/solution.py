from itertools import chain


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
            self.position[numbers[i]] = (i, row)
            index += 1
            if index == 24:
                break

    def fill_bingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def is_bingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]

    def update(self, val):
        x, y = self.position.get(val, (-1, -1))
        if x != -1 and y != -1:
            self.fill_bingo(x, y)


# Challenge 1
with open("input.txt") as file:
    content = file.read().splitlines()

drawings = [int(d) for d in content[0].split(",")]
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
        board.initialize(row, [int(value) for value in content[i].split()])
        row += 1

isBingo = False
winnerIndex = None
winningDraw = drawIndex = 0

for dIdx, drawing in enumerate(drawings):
    for idx, board in enumerate(boards):
        board.update(int(drawing))
        if board.is_bingo():
            winnerIndex = idx
            winningDraw = drawing
            isBingo = True
            break
    if isBingo is True:
        drawIndex = dIdx
        break

result = sum([z for z in list(chain.from_iterable(boards[winnerIndex].board)) if z not in drawings[:drawIndex + 1]]) \
         * winningDraw
print("Solution: " + str(result))

# Challenge 2
