def winning(board):
    for i in range(5):
        ok = True
        for j in range(5):
            if board[i][j] != -1:
                ok = False
                break
        if ok:
            return True
    for i in range(5):
        ok = True
        for j in range(5):
            if board[j][i] != -1:
                ok = False
                break
        if ok:
            return True


def mark(board, val):
    for i in range(5):
        for j in range(5):
            if board[i][j] == val:
                board[i][j] = -1
    return board


def sum_unmarked(board):
    ret = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                ret += board[i][j]
    return ret


# Part 1:
# with open("input.in") as file:
#     lines = file.readlines()
#     nums = list(map(int, lines[0].split(",")))
#     boards = []
#     for i in range(1, len(lines), 6):
#         board = []
#         for j in range(i + 1, i + 6):
#             k = list(map(int, lines[j].split()))
#             board.append(k)
#         boards.append(board)
#     min_step = 1000000000
#     for board in boards:
#         step = 0
#         while (step < len(nums)) and (not winning(board)):
#             board = mark(board, nums[step])
#             step += 1
#         if winning(board):
#             if step < min_step:
#                 min_step = step
#                 ans = sum_unmarked(board) * nums[step - 1]

#     print(ans)

with open("input.in") as file:
    lines = file.readlines()
    nums = list(map(int, lines[0].split(",")))
    boards = []
    for i in range(1, len(lines), 6):
        board = []
        for j in range(i + 1, i + 6):
            k = list(map(int, lines[j].split()))
            board.append(k)
        boards.append(board)
    max_step = -1
    for board in boards:
        step = 0
        while (step < len(nums)) and (not winning(board)):
            board = mark(board, nums[step])
            step += 1
        if winning(board):
            if step > max_step:
                max_step = step
                ans = sum_unmarked(board) * nums[step - 1]

    print(ans)
