def solve(p1, p2):
    startPos = [p1, p2]
    scores = [0, 0]
    i = 0
    s = 0
    while True:
        c = i % 2
        d = 3 * s + 6
        s += 3
        s %= 100
        startPos[c] = ((startPos[c] + d) - 1) % 10 + 1
        scores[c] += startPos[c]
        if scores[c] >= 1000: break
        i += 3
    print((i + 3) * min(scores))

if __name__ == '__main__':
    solve(10, 2)
