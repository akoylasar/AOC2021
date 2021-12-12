import time

def solve():
    with open('day7.txt', 'r') as file:
        pos = [int(x) for x in file.readline().strip().split(',')]
    pos.sort()
    c = len(pos)
    median = pos[c // 2] if c % 2 else (pos[c // 2 - 1] + pos[c // 2]) // 2
    fuel = sum([abs(f - median) for f in pos])
    print(fuel)

if __name__ == '__main__':
    start = time.time()
    solve()
    print("%s seconds" % (time.time() - start))