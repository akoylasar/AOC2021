import time
from collections import defaultdict

# TODO: implement without recursion
def solve(graph):
    paths = []
    def traverse(path):
        last = path[-1]
        if last == 'end':
            paths.append(path)
        else:
            for next in graph[last]:
                a = next.isupper()
                b = next.islower() and next not in path
                s = [x for x in path if x.islower()]
                c = next.islower() and next in path and next != 'start' and next != 'end' and len(s) == len(set(s)) # TODO: fix this crap.
                if a or b or c:
                    newPath = path[:]
                    newPath.append(next)
                    traverse(newPath)
    traverse(['start'])
    print(len(paths))

if __name__ == '__main__':
    with open('day12.txt', 'r') as file:
        nput = defaultdict(set)
        while True:
            line = file.readline()
            if not line:
                break
            verts = line.strip().split('-')
            for i in range(2):
                nput[verts[1 - i]].add(verts[i])
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))