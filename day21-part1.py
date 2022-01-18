def solve(startPos):
    base = (6, 15)
    scores = [0, 0]
    i = 0
    flip = 0
    while True:
        n = i % 11
        c = i % 2
        startPos[c] = (startPos[c] % 10) + 18 * n + base[1 - c if flip else c]
        scores[c] += startPos[c]
         scores[c] >= 1000:
            break
        i += 1
        flip = int(i % 33 == 0)

