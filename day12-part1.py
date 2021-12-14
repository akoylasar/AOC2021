import time
from collections import defaultdict

def solve(nput):
    paths = []
    def traverse(path):
        last = path[-1]
        if last == 'end':
            paths.append(path)
        else:
            for next in nput[last]:
                if next.isupper() or (next.islower() and next not in path):
                    newPath = path[:]
                    newPath.append(next)
                    traverse(newPath)
    traverse(['start'])
    print(len(paths))

def solveNonRecursively(graph):
    numPaths = 0
    stack = ['start']
    counters = [0]
    while stack:
        node = stack[-1]
        i = counters[-1]
        neighbours = graph[node]
        pop = True
        while i < len(neighbours):
            cave = neighbours[i]
            if cave == 'end':
                numPaths += 1
            else:
                isBig = cave.isupper()
                smallAndNotVisited = not isBig and cave not in stack
                if isBig or smallAndNotVisited:
                    counters[-1] = i + 1 # save up "sack frame" and add new
                    stack.append(cave)
                    counters.append(0)
                    pop = False
                    break
            i += 1
        if pop:
            stack.pop()
            counters.pop()
    print(numPaths)

if __name__ == '__main__':
    with open('day12.txt', 'r') as file:
        nput = defaultdict(list)
        while True:
            line = file.readline()
            if not line:
                break
            verts = line.strip().split('-')
            for i in range(2):
                vert = verts[i]
                node = nput[verts[1 - i]]
                if vert not in node:
                    node.append(vert)
    start = time.time()
    solveNonRecursively(nput)
    print("%s seconds" % (time.time() - start))