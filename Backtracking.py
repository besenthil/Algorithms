
SUDOKO_PUZZLE = [
    [
        [
            [1, 4, 2],
            [7, 0, 0],
            [8, 0, 5]
        ],
        [
            [0, 9, 0],
            [4, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 5],
            [0, 8, 9],
            [0, 2, 4]
        ]
    ],
    [
        [
            [2, 0, 0],
            [0, 3, 0],
            [0, 8, 0]
        ],
        [
            [0, 0, 4],
            [0, 0, 1],
            [0, 7, 2]
        ],
        [
            [8, 0, 0],
            [2, 6, 0],
            [9, 4, 1]
        ]
    ],
    [
        [
            [0, 5, 0],
            [0, 2, 8],
            [0, 7, 9]
        ],
        [
            [2, 0, 6],
            [0, 0, 9],
            [1, 0, 8]
        ],
        [
            [0, 0, 0],
            [4, 1, 0],
            [5, 3, 0]
        ]
    ],
]

symbol = [[[[0 for col in range(3)] for col in range(3)] for col in range(3)] for row in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if SUDOKO_PUZZLE[i][j][k][l]:
                    symbol[i][j][k][l] = SUDOKO_PUZZLE[i][j][k][l]

def check_in_puzzle_piece(row,column):
    for i in range(3):
        for j in range(3):
            if not symbol[row][column][i][j]:
