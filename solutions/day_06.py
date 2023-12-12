################################
###### OPTIMIZED SOLUTION ######
################################

with open('data/day_06.txt') as f:
    time, distance = [l.split()[1:] for l in f.read().strip().split('\n')]
    time_p1, distance_p1 = list(map(int, time)), list(map(int, distance))
    time_p2, distance_p2 = int(''.join(time)), int(''.join(distance))

#Part 1
result_p1 = 1
for i, t in enumerate(time_p1):
    for x in range(t):
        if (t - x) * x > distance_p1[i]:
            result_p1 *= (t - x) - x + 1
            break
#Part 2
for x in range(time_p2):
    if (time_p2 - x) * x > distance_p2:
        result_p2 = (time_p2 - x) - x + 1
        break

#Results
print(result_p1) #Part 1
print(result_p2) #Part 2


###############################
###### OUTDATED SOLUTION ######
###############################

import pandas as pd
import json

with open('data/day_06.json', 'r') as data_file:
    json_data = data_file.read()

instance_json = json.loads(json_data)
df = pd.DataFrame(instance_json, columns=['time', 'distance'])


def find_possible_holding_times(time, distance):
    possible_holding_times = []

    for wait_time in range(time + 1):
        current_speed = wait_time
        current_time = time - wait_time
        current_distance = current_time * current_speed

        if current_distance > distance:
            possible_holding_times.append(wait_time)

    return possible_holding_times


def part1():
    def find_possible_holding_times(time, distance):
        possible_holding_times = []

        for wait_time in range(time + 1):
            current_speed = wait_time
            current_time = time - wait_time
            current_distance = current_time * current_speed

            if current_distance > distance:
                possible_holding_times.append(wait_time)

        return possible_holding_times

    ways_to_beat = []

    for _, row in df.iterrows():
        time = row['time']
        distance = row['distance']

        ways_per_row = len(find_possible_holding_times(time, distance))
        ways_to_beat.append(ways_per_row)

    result = 1
    for x in ways_to_beat:
        result = result * x

    return result


def part2():
    time = int(''.join(map(str, instance_json['time'])))
    distance = int(''.join(map(str, instance_json['distance'])))

    result = len(find_possible_holding_times(time, distance))
    return result

print(part1())
print(part2())
