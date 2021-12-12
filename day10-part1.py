import time

pointTable = {')': tuple((3, '(')),
              ']': tuple((57, '[')),
              '}': tuple((1197, '{')),
              '>': tuple((25137, '<'))}

def solve(lines):
    points = []
    for line in lines:
        stop = False
        stack = []
        for c in line:
            if c == '(' or c == '[' or c == '{' or c == '<':
                stack.append(c)
            else:
                if stack[-1] != pointTable[c][1]:
                    points.append(pointTable[c][0])
                    stop = True
                    break
                stack.pop()
        if stop:
            continue
    print (sum(points))

if __name__ == '__main__':
    with open('day10.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))