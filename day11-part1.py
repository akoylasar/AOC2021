import time
import numpy as np

def solve(nput, numSteps):
    totalFlashes = 0
    height = len(nput)
    width = len(nput[0])
    def updateGrid(h, w, flashed):
        if h < 0 or h >= height or w < 0 or w >= width:
            return 0
        if flashed[h][w]:
            return 0
        if nput[h][w] > 9:
            flashed[h][w] = 1
            nput[h][w] = 0
            l = updateGrid(h, w - 1, flashed)
            r = updateGrid(h, w + 1, flashed)
            u = updateGrid(h + 1, w, flashed)
            d = updateGrid(h - 1, w, flashed)
            ld = updateGrid(h - 1, w - 1, flashed)
            lu = updateGrid(h + 1, w - 1, flashed)
            rd = updateGrid(h - 1, w + 1, flashed)
            ru = updateGrid(h + 1, w + 1, flashed)
            return 1 + l + r + u + d + ld + lu + rd + ru
        else:
            nput[h][w] += 1
            if nput[h][w] > 9:
                return updateGrid(h, w, flashed)
        return 0
    for i in range(numSteps):
        nput = np.array([x + 1 for x in nput])
        flashed = np.zeros((height, width), dtype=int)
        toFlash = [tuple((j, i)) for j in range(height) for i in range(width) if nput[j][i] > 9]
        for oct in toFlash:
            totalFlashes += updateGrid(oct[0], oct[1], flashed)
    print (totalFlashes)

if __name__ == '__main__':
    with open('day11.txt', 'r') as file:
        nput = np.array([[int(n) for n in l.strip()] for l in file.readlines()])
    start = time.time()
    solve(nput, 100)
    print("%s seconds" % (time.time() - start))