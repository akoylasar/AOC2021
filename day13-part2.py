import time
import numpy as np

def solve(points, instructions):
    dim = np.amax(points, 0) - np.amin(points, 0) + [1, 1]
    for axis, pos in instructions:
        points = fold(points, axis, pos, dim)
    def fouadHash(p):
        n = p[0] + p[1]
        return (n * (n + 1) // 2) + p[1]
    hashed = [fouadHash(p) for p in points]
    for j in range(dim[1]):
        for i in range(dim[0]):
            if fouadHash((i, j)) in hashed:
                print('#', end='')
            else:
                print('.', end='')
        print()

def fold(points, axis, pos, dim):
    def reflect(p):
        p[axis] = dim[axis] - p[axis] - 1 if p[axis] > pos else p[axis]
        return p
    points = np.apply_along_axis(reflect, 1, points)
    dim[axis] = dim[axis] // 2
    return points

if __name__ == '__main__':
    with open('day13.txt', 'r') as file:
        points = []
        instructions = []
        while True:
            line = file.readline()
            if line == '\n':
                break
            points.append([int(x) for x in line.strip().split(',')])
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip().split()[2].split('=')
            instructions.append(tuple((1 if line[0] == 'y' else 0, int(line[1]))))
    start = time.time()
    points = np.array(points)
    solve(points, instructions)
    print("%s seconds" % (time.time() - start))