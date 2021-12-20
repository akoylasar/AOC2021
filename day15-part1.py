import math
import numpy as np
import time
import heapq as hq

def solve(weights):
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
    w, h = weights.shape
    source = (0, 0)
    dest = (w - 1, h - 1)
    dist = np.full(weights.shape, math.inf)
    dist[source] = 0
    Q = [(0, source)]
    hq.heapify(Q)
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
                    hq.heappush(Q, (alt, v))
    print(dist[dest])

if __name__ == '__main__':
    with open('day15.txt', 'r') as file:
        weights = np.array([[int(s) for s in line.strip()] for line in file.readlines()])
    start = time.time()
    solve(weights)
    print("%s seconds" % (time.time() - start))