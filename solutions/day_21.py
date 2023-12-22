from collections import deque

### PART 1 ###
def count_grid(r, c, s):
# State = (r,c, remain steps)
    queue = deque([(r, c, s)])
    seen = set()
    count = 0

    while queue:
        r, c, s = queue.popleft()

        if (r, c) in seen or s < 0:
            continue

        seen.add((r, c))

        if s % 2 == 0:
            count += 1

        for dr, dc in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            next_r, next_c = r + dr, c + dc

            if 0 <= next_r < size and 0 <= next_c < size and grid[next_r][next_c] != '#':
                queue.append((next_r, next_c, s - 1))

    return count

### PART 2 ###
def count_repeated_grid(size, steps, radius):
    right_corner = count_grid(size // 2, 0, steps - (size // 2 + 1) - ((radius - 1) * size))
    left_corner = count_grid(size // 2, size - 1, steps - (size // 2 + 1) - ((radius - 1) * size))
    top_corner = count_grid(size - 1, size // 2, steps - (size // 2 + 1) - ((radius - 1) * size))
    bottom_corner = count_grid(0, size // 2, steps - (size // 2 + 1) - ((radius - 1) * size))

    odd_blocks = count_grid(0, 0, 2 * size + 11)
    even_blocks = count_grid(0, 0, 2 * size + 10)

    edge_top_right_out = count_grid(size - 1, 0, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
    edge_top_left_out = count_grid(size - 1, size - 1, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
    edge_bottom_right_out = count_grid(0, 0, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))
    edge_bottom_left_out = count_grid(0, size - 1, steps - ((radius - 1) * size) - 2 * (size // 2 + 1))

    edge_top_right_in = count_grid(size - 1, 0, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
    edge_top_left_in = count_grid(size - 1, size - 1, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
    edge_bottom_right_in = count_grid(0, 0, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))
    edge_bottom_left_in = count_grid(0, size - 1, steps - ((radius - 2) * size) - 2 * (size // 2 + 1))

    count = right_corner + left_corner + top_corner + bottom_corner
    count += odd_blocks * pow(radius - 1, 2)
    count += even_blocks * pow(radius, 2)
    count += (edge_top_right_out + edge_top_left_out + edge_bottom_right_out + edge_bottom_left_out) * radius
    count += (edge_top_right_in + edge_top_left_in + edge_bottom_right_in + edge_bottom_left_in) * (radius - 1)

    return count


with open('data/day_21.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Find size
size = len(grid)

# Check if grid is square shaped
assert size == len(grid[0])
# Check if middle row (containing 'S') does not contain any '#'
assert all(c != '#' for c in grid[size // 2])
# Check if middle column (containing 'S') does not contain any '#'
assert all(c != '#' for c in list(zip(*grid))[size // 2])

# Find start
(start,) = [(r, c) for r, row in enumerate(grid)
                   for c, char in enumerate(row) if grid[r][c] == 'S']

### PART 1 ###
steps = 64

part1 = count_grid(*start, steps)
print(f'Part 1: {part1}')

### PART 2 ###
steps = 26501365
radius = steps // size

part2 = count_repeated_grid(size, steps,radius)
print(f'Part 2: {part2}')
