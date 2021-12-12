import time

charMap = {')': '(', ']': '[', '}': '{', '>': '<'}
pointMap = {'(': 1, '[': 2, '{': 3,'<': 4}

def solve(lines):
    incompletes = []
    for line in lines:
        stop = False
        stack = []
        for c in line:
            if c == '(' or c == '[' or c == '{' or c == '<':
                stack.append(c)
            else:
                if stack[-1] != charMap[c]:
                    stop = True
                    break
                stack.pop()
        if stop:
            continue
        incompletes.append(''.join(stack))
    def calcScore(entry):
        s = 0
        for i in range(len(entry)):
            s *= 5
            c = entry[len(entry) - i - 1]
            s += pointMap[c]
        return s
    scores = list(map(calcScore, incompletes))
    scores.sort()
    print(scores[len(scores) // 2])

if __name__ == '__main__':
    with open('day10.txt', 'r') as file:
        lines = [l.strip() for l in file.readlines()]
    start = time.time()
    solve(lines)
    print("%s seconds" % (time.time() - start))