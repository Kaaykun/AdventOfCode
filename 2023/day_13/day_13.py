import numpy as np

def find_mirror_point(p, multiplier, part):
    value = 0
    for r in range(1, p.shape[0]):
        block_size = min(p.shape[0] - r, r)
        top_segment = p[r - block_size:r]
        top_segment_flipped = np.flip(top_segment, axis=0)
        bot_segment = p[r:r + block_size]
        if part == 1:
            if np.all(top_segment_flipped == bot_segment):
                value = r * multiplier
        if part == 2:
            if list((top_segment_flipped == bot_segment).flatten()).count(False) == 1:
                value = r * multiplier
    return value

with open("data/day_13.txt", "r") as file:
    data = file.read()
puzzles = [i.split('\n') for i in data.split('\n\n')]
# Remove last empty row automatically added to .txt file
puzzles[-1] = puzzles[-1][:-1]

for p in range(0 , len(puzzles)):
    for r in range(0, len(puzzles[p])):
        puzzles[p][r] = puzzles[p][r].replace('.', '0')
        puzzles[p][r] = puzzles[p][r].replace('#', '1')
        puzzles[p][r] = [int(x) for x in puzzles[p][r]]
    puzzles[p] = np.array(puzzles[p])

parts = [1, 2]
for part in parts:
    point = 0
    for p in puzzles:
        point += find_mirror_point(p, 100, part)
        point += find_mirror_point(np.rot90(p,-1), 1, part)
    print("part: ", part, point)
