def solve():
    with open('day6.txt', 'r') as file:
        fishes = [int(x) for x in file.readline().strip().split(',')]
    for i in range(80):
        newFishes = []
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                newFishes.append(8)
            else:
                fishes[i] = fish - 1;
        fishes.extend(newFishes)
    print(len(fishes))

if __name__ == '__main__':
    solve()