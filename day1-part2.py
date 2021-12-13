import time

def solve(depths):
    print(sum([1 if((depths[i + 3] - depths[i]) > 0) else 0 for i in range(len(depths) - 3)]))

if __name__ == '__main__':
    with open('day1.txt', 'r') as file:
        depths = [int(n) for n in file.readlines()]
    start = time.time()
    solve(depths)
    print("%s seconds" % (time.time() - start))