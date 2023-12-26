with open('data/day_10.txt') as f:
    pipes = f.read().splitlines()

def find_next(cur, x, y):
    if cur == "7":
        return [[x-1, y], [x, y+1]]
    elif cur == "J":
        return [[x-1, y], [x, y-1]]
    elif cur == "F":
        return [[x+1, y], [x, y+1]]
    elif cur == "L":
        return [[x+1, y], [x, y-1]]
    elif cur == "-":
        return [[x-1, y], [x+1, y]]
    elif cur == "|":
        return [[x, y+1],[x, y-1]]


for i in range(len(pipes)):
    if "S" in pipes[i]:
        start = [pipes[i].index('S'), i]

stepmap = [['.'] * len(pipe) for pipe in pipes]
steps, cur_queue, next_queue = 1, [], []

shape_flag = 0
shape_map = {11: "-", 101: "J", 1001: "7", 110: "L", 1010: "F", 1100: "|"}

if pipes[start[1]][start[0] - 1] in ["F", "L", "-"]:
    shape_flag += 1
    cur_queue.append((start[0]-1, start[1]))
if pipes[start[1]][start[0] + 1] in ["J", "7", "-"]:
    shape_flag += 10
    cur_queue.append((start[0]+1, start[1]))
if pipes[start[1] - 1][start[0]] in ["F", "7", "|"]:
    shape_flag += 100
    cur_queue.append((start[0], start[1]-1))
if pipes[start[1]+1][start[0]] in ["J", "L", "|"]:
    shape_flag += 1000
    cur_queue.append((start[0], start[1]+1))

stepmap[start[1]][start[0]] = shape_map[shape_flag]

while cur_queue:
    x, y = cur_queue.pop()
    stepmap[y][x] = pipes[y][x]
    next_steps = find_next(pipes[y][x], x, y)
    for step in next_steps:
        if stepmap[step[1]][step[0]] == ".":
            next_queue.append(step)

    # Part 1 solution
    if not cur_queue:
        cur_queue = next_queue
        next_queue = []
        steps += 1

newMap, newlines = [], []
for j, line in enumerate(stepmap):
    i = 0

    newline = []
    while i < len(line):
        if line[i] in ["L", "F", "-"]: line.insert(i+1, "-")
        else: line.insert(i+1, ".")
        if line[i] in ["F", "|", "7"]: newline += ["|", "."]
        else: newline += [".", "."]
        i += 2
    newlines.append(newline)

bigmap = [None] * (len(stepmap)*2)
bigmap[::2] = stepmap
bigmap[1::2] = newlines
bigmap.insert(0, ["."] * len(bigmap[0]))

cur_queue = [[0,0]]
while cur_queue:
    x, y = cur_queue.pop()
    bigmap[y][x] = "O"
    try:
        if bigmap[y][x-1] == ".":
            cur_queue.append([x-1, y])
    except: pass
    try:
        if bigmap[y][x+1] == ".":
            cur_queue.append([x+1, y])
    except:pass
    try:
        if bigmap[y+1][x] == ".":
            cur_queue.append([x, y+1])
    except:pass
    try:
        if bigmap[y-1][x] == ".":
            cur_queue.append([x, y-1])
    except:pass


print(steps-1)
print(sum(line[::2].count(".") for line in stepmap))
