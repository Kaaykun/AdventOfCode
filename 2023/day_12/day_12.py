from functools import cache

# Define a function to count arrangements based on conditions and group sizes
@cache  # Cache function results
def count_arrangements(condition, group_size, h=0):
    # Base case: If no condition is left to check
    if not condition:
        # Return True if both group_size and h are zero, else return False
        return not group_size and not h

    # Initialize count of valid arrangements
    n = 0

    # If the first character in the condition is '#' or '?'
    if condition[0] in ("#", "?"):
        # Recursively explore arrangements skipping the first character in condition
        # Increase height h by 1 and continue
        n += count_arrangements(condition[1:], group_size, h + 1)

    # If the first character in the condition is '.' or '?' and meets certain conditions
    if condition[0] in (".", "?") and (group_size and group_size[0] == h or not h):
        # Recursively explore arrangements skipping the first character in condition
        # Adjust group sizes based on height h or keep the group size unchanged
        n += count_arrangements(condition[1:], group_size[1:] if h else group_size)

    # Return the total count of valid arrangements found
    return n


# Read input from a file and process it
with open("data/day_12.txt") as f:
    # Split the lines and store conditions with their respective group sizes as tuples
    input_lines = [line.split() for line in f.read().splitlines()]
    input_lines = [(condition, tuple(int(group_sizes) for group_sizes in line.split(","))) for condition, line in input_lines]

# Calculate and print the sum of arrangements based on given conditions and group sizes
print(sum(count_arrangements(condition + ".", group_size, 0) for condition, group_size in input_lines))
print(sum(count_arrangements("?".join([condition] * 5) + ".", group_size * 5) for condition, group_size in input_lines))
