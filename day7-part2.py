import math
import time

def solve(pos):
    avg = sum(pos) / len(pos)
    fuels1 = [abs(f - math.floor(avg)) for f in pos]
    fuels2 = [abs(f - math.ceil(avg)) for f in pos]
    def arith(x):
        return (x // 2) * (x + 1) + (x % 2) * ((x + 1) // 2)
    fuel1 = sum(arith(x) for x in fuels1)
    fuel2 = sum(arith(x) for x in fuels2)
    print(min(fuel1, fuel2))

def validate(pos):
    fuel = math.inf
    n = 0
    for i in range(min(pos), max(pos) + 1):
        fuels = [abs(f - i) for f in pos]
        c = sum(int(x * ((x + 1) / 2)) for x in fuels)
        if c <= fuel:
            fuel = c
            n = i
    print(n, fuel)

if __name__ == '__main__':
    with open('day7.txt', 'r') as file:
        pos = [int(x) for x in file.readline().strip().split(',')]
    start = time.time()
    solve(pos)
    print("%s seconds" % (time.time() - start))
