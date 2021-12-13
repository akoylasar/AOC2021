import numpy as np
import time

def solve(drawOrder, boards):
    boardsFlags = [np.ones((5, 5), dtype=int) for i in range(len(boards))]  # 1 means not marked (convenient later)
    print(playBingo(drawOrder, boards, boardsFlags))

def playBingo(drawOrder, boards, boardsFlags):
    a = 0
    won = []
    for n in drawOrder:
        for i, board in enumerate(boards):
            if updateBoard(n, board, boardsFlags[i]) and i not in won:
                won.append(i)
                a = n * sum((board * boardsFlags[i]).flatten())
    return a

def updateBoard(n, board, boardFlags):
    indices = np.where(board == n)
    if indices[0].size > 0:
        boardFlags[indices[0][0], indices[1][0]] = 0  # 0 means marked
        for i in range(5):
            if ((sum(boardFlags[i]) == 0) or (sum(boardFlags[0:, i]) == 0)):
                return True
    return False

if __name__ == '__main__':
    with open('day4.txt', 'r') as file:
        lines = list(line for line in (l.strip() for l in file) if line)
    drawOrder = tuple(int(n) for n in lines[0].split(','))
    boards = [np.array([[int(x) for x in l.split()] for l in lines[i:i + 5]]) for i in range(1, len(lines) - 1, 5)]
    start = time.time()
    solve(drawOrder, boards)
    print("%s seconds" % (time.time() - start))