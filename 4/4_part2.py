boards = []
with open("input.txt") as f:
    numbers = [int(i) for i in f.readline().split(",")]
    curr_board = []
    for i in f.readlines():
        i = i.strip()
        if i == "":
            if len(curr_board) > 0:
                boards.append(curr_board)
            curr_board = []
            continue
        curr_board.append([int(j) for j in i.split()])
    if len(curr_board) > 0:
        boards.append(curr_board)

picked = []


def has_won(board):
    for i in range(5):
        did_win = True
        for j in range(5):
            if board[i][j] not in picked:
                did_win = False
        if did_win:
            return True
    for i in range(5):
        did_win = True
        for j in range(5):
            if board[j][i] not in picked:
                did_win = False
        if did_win:
            return True


winning_boards = []
last = []
for number in numbers:
    picked.append(number)

    for board in boards:
        if has_won(board) and board not in winning_boards:
            winning_boards.append(board)
    if len(winning_boards) == len(boards):
        print(winning_boards[-1], picked[-1])
        print(
            number,
            sum(
                number
                for row in winning_boards[-1]
                for number in row
                if number not in picked
            ),
        )
        print(
            number
            * sum(
                number
                for row in winning_boards[-1]
                for number in row
                if number not in picked
            )
        )
        exit()
