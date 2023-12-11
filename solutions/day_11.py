with open('data/day_11.txt') as f:
    data = [line.rstrip() for line in f]

# Extract coordinates of '#' from the input
coordinates = []
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == '#':
            coordinates.append((x, y))

xs, ys = zip(*coordinates)

def dist(ps):
    ps = [sum((l, 1)[p in ps] for p in range(p)) for p in ps]
    return sum(abs(a-b) for a in ps for b in ps)//2

for l in 2, 1_000_000:
    print(sum(map(dist, [xs, ys])))
