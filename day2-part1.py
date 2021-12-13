import time

def solve(submarineRoute):
    x = 0
    y = 0
    for s in submarineRoute:
        if (s[0] == 'forward'):
            x += int(s[1])
        elif (s[0] == 'down'):
            y += int(s[1])
        else: # (i[0] == 'up')
            y -= int(s[1])
    print(x * y)

if __name__ == '__main__':
    with open('day2.txt', 'r') as file:
        nput = [n.split() for n in file.readlines()]
    start = time.time()
    solve(nput)
    print("%s seconds" % (time.time() - start))