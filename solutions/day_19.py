import math

operators = {'<': int.__lt__, '>': int.__gt__}

def apply_workflows(part, workflow):
    if workflow in 'AR':
        return workflow

    for category, operator, value, target in workflows[workflow]:
        if category == 'default' or operators[operator](part[category], value):
            return apply_workflows(part, workflow=target)

    assert False

def apply_workflows_ranges(ranges, workflow):
    if workflow == 'R':
        return 0

    if workflow == 'A':
        return math.prod(stop - start for start, stop in ranges.values())

    total = 0

    for category, operator, value, target in workflows[workflow]:
        if category == 'default':
            total += apply_workflows_ranges(ranges, workflow=target)
            continue

        start, stop = ranges[category]

        if operator == '<':
            match_range = (start, min(value, stop))
            miss_range = (max(value, start), stop)
        else:
            match_range = (max(value + 1, start), stop)
            miss_range = (start, min(value + 1, stop))

        if match_range[0] < match_range[1]:
            next_ranges = dict(ranges)
            next_ranges[category] = match_range
            total += apply_workflows_ranges(next_ranges, workflow=target)

        if miss_range[0] < miss_range[1]:
            ranges = dict(ranges)
            ranges[category] = miss_range
        else:
            break

    return total

# Read input file
with open('data/day_19.txt', 'r') as file:
    raw_workflows, raw_parts = file.read().split('\n\n')

# Parse workflows
workflows = {}
for line in raw_workflows.splitlines():
    #Example line: px{a<2006:qkq,m>2090:A,rfg}
    name, raw_rules = line.rstrip('}').split('{')
    rules = []

    for rule in raw_rules.split(','):
        # If last rule is reached
        if ':' not in rule:
            rules.append(('default', None, None, rule))
            continue

        # Split each rule into condition ('a<2006') and target ('qkq')
        condition, target = rule.split(':')

        # Split each condition into category ('a'), operator ('<') and value (2006)
        category = condition[0]
        operator = condition[1]
        value = int(condition[2:])

        # Check for errors
        assert operator in '<>'
        assert value >= 0
        rules.append((category, operator, value, target))

    workflows[name] = rules

# Loop over parts, if accept add to total
part1 = 0

for line in raw_parts.splitlines():
    # Example line: {x=787,m=2655,a=1222,s=2876}
    values = line.strip('{}').split(',')
    part = {}
    for value in values:
        v_type, v = value.split('=')
        part[v_type] = int(v)
    if apply_workflows(part, workflow='in') == 'A':
        part1 += sum(part.values())

part2 = apply_workflows_ranges({k: (1, 4001) for k in 'xmas'}, workflow='in')

print('Part 1:', part1)
print('Part 2:', part2)
