import numpy as np
import collections

def getline(line, split):
    out = []
    split_line = line.replace("\n", "").split(split)
    #print(split_line)
    for item in split_line:
        if len(item) > 0:
            try:
                out.append((int)(item))
            except Exception as e:
                print(e)
    return out

def check_bingo(item):
    for i in range(0, len(item[1])):
        count = collections.Counter(item[1][i])
        if count[1] == len(item[1]):
            #print("Row BINGO!")
            return True

    for i in range(0, len(item[1][0])):
        count = collections.Counter(item[1][:,i])
        #print(count)
        if count[1] == len(item[1][0]):
            #print("Col BINGO!")
            return True

    return False

def run_bingo_win(called, boards):
    for call in called:
        #print(call)
        for board in boards:
            r, c = np.where(board[0] == call)
            if len(r) > 0 and len(c) > 0:
                board[1][np.where(board[0] == call)] = 1
            if check_bingo(board):
                return board, call

def run_bingo_lose(called, boards):
    for call in called:
        checked = []
        for board in boards:
            r, c = np.where(board[0] == call)
            if len(r) > 0 and len(c) > 0:
                board[1][np.where(board[0] == call)] = 1
            bingo = check_bingo(board)
            if not bingo:
                checked.append(board)
            elif(len(boards) == 1):
                return board, call
        boards = checked

called = []
boards = []
board = []
board_called = np.zeros([5,5])

with open("data\d4e2.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            called = getline(line, ',')
        elif line != '\n':
            board.append(getline(line, ' '))
        else:
            if len(board) > 0:
                boards.append([np.array(board), np.zeros_like(board)])
            board = []
    boards.append([np.array(board), np.zeros_like(board)])

board, call = run_bingo_win(called, boards)
uncalled = np.sum(board[0][np.where(board[1] == 0)])
score = uncalled * call

print("~~~~~~~ Part 1 ~~~~~~~")
print("Won with board: \n", board[0])
print("Score:", score, "({0} * {1})".format(uncalled, call))


board, call = run_bingo_lose(called, boards)
uncalled = np.sum(board[0][np.where(board[1] == 0)])
score = uncalled * call

print("~~~~~~~ Part 2 ~~~~~~~")
print("Won with board: \n", board[0])
print("Score:", score, "({0} * {1})".format(uncalled, call))