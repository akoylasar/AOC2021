import math
import numpy as np
import time
import heapq as hq

def solve(weights, source, dest):
    w, h = weights.shape
    def getNeighbours(p):
        n = []
        if p[0] == 0:
            n.append((1, p[1]))
        elif p[0] == w - 1:
            n.append((w - 2, p[1]))
        else:
            n.append((p[0] - 1, p[1]))
            n.append((p[0] + 1, p[1]))
        if p[1] == 0:
            n.append((p[0], 1))
        elif p[1] == h - 1:
            n.append((p[0], h - 2))
        else:
            n.append((p[0], p[1] - 1))
            n.append((p[0], p[1] + 1))
        return n
    # Dijkstra # https://cs.stackexchange.com/questions/118388/dijkstra-without-decrease-key
    dist = np.full(weights.shape, math.inf)
    dist[source] = 0
    Q = [(0, source)]
    hq.heapify(Q)
    # prev = np.full(weights.shape, None)
    while len(Q) != 0:
        k, u = hq.heappop(Q)
        if u == dest:
            break
        if k == dist[u]:
            neighbours = getNeighbours(u)
            for v in neighbours:
                alt = dist[u] + weights[v]
                cost = dist[v]
                if alt < cost:
                    dist[v] = alt
                    # prev[v] = u
                    hq.heappush(Q, (alt, v))
    print(dist[dest])

if __name__ == '__main__':
    with open('day15.txt', 'r') as file:
        weights = np.array([[int(s) for s in line.strip()] for line in file.readlines()])
    w, h = weights.shape
    fullMap = np.tile(weights, (5, 5))
    for j in range(5):
        for i in range(5):
            tileStart = (i * w, j * h)
            incCount = i + j
            for k in range(h):
                for l in range(w):
                    p = (tileStart[0] + l, tileStart[1] + k)
                    newWeight = weights[k][l]
                    for n in range(incCount):
                        newWeight += 1
                        newWeight = 1 if newWeight > 9 else newWeight
                    fullMap[p] = newWeight
    source = (0, 0)
    dest = (fullMap.shape[0] - 1, fullMap.shape[1] - 1)
    start = time.time()
    solve(fullMap, source, dest)
    print("%s seconds" % (time.time() - start))