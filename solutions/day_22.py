from collections import deque


class Brick:
    def __init__(self, line) -> None:
        # Example line: 6,5,33~8,5,33
        points = [list(map(int, p.split(','))) for p in line.strip().split('~')]
        p1, p2 = sorted(points, key=lambda p: p[2])
        self.x1, self.y1, self.z1 = p1
        self.x2, self.y2, self.z2 = p2
        assert self.z1 <= self.z2

        self.supports = set()
        self.supported_by = set()

    def __repr__(self) -> str:
        return f'<Brick {(self.x1, self.y1, self.z1)}, {(self.x2, self.y2, self.z2)}>'

    def overlaps(self, other) -> bool:
        return (
            max(self.x1, other.x1) <= min(self.x2, other.x2) and
            max(self.y1, other.y1) <= min(self.y2, other.y2)
        )


with open('data/day_22.txt', 'r') as file:
    lines = file.readlines()

bricks = sorted([Brick(line) for line in lines], key=lambda b: b.z1)

# Falling bricks
for i, brick in enumerate(bricks):
    floor = 0
    for other in bricks[:i]:
        if brick.overlaps(other):
            floor = max(floor, other.z2 + 1)
    fall_distance = brick.z1 - floor
    brick.z1 -= fall_distance
    brick.z2 -= fall_distance

bricks.sort(key=lambda b: b.z1)

# Supporting / Supported bricks
for i, brick in enumerate(bricks):
    for other in bricks[:i]:
        if brick.overlaps(other) and other.z2 == brick.z1 - 1:
            brick.supported_by.add(other)
            other.supports.add(brick)

### PART 1 ###
part1 = sum(all(len(other.supported_by) > 1 for other in brick.supports) for brick in bricks)

print(f'Part 1: {part1}')

### PART 2 ###
part2 = 0
for brick in bricks:
    queue = deque([brick])
    is_falling = set()

    while queue:
        brick = queue.popleft()
        if brick in is_falling:
            continue
        is_falling.add(brick)

        for suported_brick in brick.supports:
            if suported_brick.supported_by.issubset(is_falling):
                queue.append(suported_brick)

    part2 += len(is_falling) - 1

print(f'Part 2: {part2}')
