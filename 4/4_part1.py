boards = []
with open('input.txt') as f:
    numbers = [int(i) for i in f.readline().split(",")]
    curr_board = []
    for i in f.readlines():
        i = i.strip()
        if i == '':
            if len(curr_board) > 0:
                boards.append(curr_board)
            curr_board = []
            continue
        curr_board.append([int(j) for j in i.split()])
    if len(curr_board) > 0:
        boards.append(curr_board)

for number in numbers:
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == number:
                    board[i][j] = 'X'
        for row in board:
            if all(num == 'X' for num in row):
                print(number * sum(number for row in board for number in row if number != 'X'))
                print()
                exit()
