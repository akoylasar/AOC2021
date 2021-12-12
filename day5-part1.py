import numpy as np
import re

def solve():
    ## in the problem y is vertical (maps to rows in array) and well x is ...
    with open('day5.txt', 'r') as file:
        lines = list(line for line in (l.strip() for l in file) if line)
    nput = np.array([[int(x) for x in re.split(',| -> ', l)] for l in lines])
    board = np.zeros((max(max(nput[:, 1]), max(nput[:, 3])) + 1,
                      max(max(nput[:, 0]), max(nput[:, 2])) + 1),  dtype = int)
    for seg in nput:
        if seg[1] == seg[3]: # visually horizontal
            for i in range(min(seg[0], seg[2]),
                           max(seg[0], seg[2]) + 1):
                board[seg[1]][i] += 1
        if seg[0] == seg[2]: # visually vertical
            for i in range(min(seg[1], seg[3]),
                           max(seg[1], seg[3]) + 1):
                board[i][seg[0]] += 1
    print(len([x for x in board.flatten() if x > 1]))

if __name__ == '__main__':
    solve()