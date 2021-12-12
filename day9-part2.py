import time
import numpy as np

def solve(lines):
    # pad edges with zeros
    width = len(lines[0].strip("\n"))
    height = len(lines)
    inf = 10
    hmap = [[inf] * (width + 2)]
    for line in lines:
        row = [inf]
        row.extend(int(n) for n in line.strip("\n"))
        row.append(inf)
        hmap.append(row)
    hmap.append([inf] * (width + 2))
    convOp = lambda x, a, b, c, d: int(x < a) + int(x < b) + int(x < c) + int(x < d)
    lowPoints = []
    i = 1
    while i < height + 1:
        j = 1
        while j < width + 1:
            if (convOp(hmap[i][j],
                       hmap[i - 1][j],
                       hmap[i + 1][j],
                       hmap[i][j - 1],
                       hmap[i][j + 1]) == 4):
                lowPoints.append((j - 1, i - 1))
                j += 2
                continue
            j += 1
        i += 1
    visited = np.zeros((height, width), dtype = int)
    def getNumLocations(w, h, col):
        if h < 0 or h >= height or w < 0 or w >= width:
            return 0
        if (hmap[h + 1][w + 1] == 9):
            return 0
        if (visited[h][w]):
            return 0
        visited[h][w] = col
        l = getNumLocations(w - 1, h, col)
        r = getNumLocations(w + 1, h, col)
        u = getNumLocations(w, h + 1, col)
        d = getNumLocations(w, h - 1, col)
        return 1 + l + r + u + d

    basinSizes = [getNumLocations(p[0], p[1], i + 1) for i, p in enumerate(lowPoints)]
    basinSizes.sort()
    s = basinSizes[-1] * basinSizes[-2] *  basinSizes[-3]
    print(s)

if __name__ == '__main__':
    with open('day9.txt', 'r') as file:
        lines = file.readlines()
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))