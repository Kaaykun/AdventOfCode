dig_plan = list(map(str.split, open('data/day_18.txt')))

mapping = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),
           '0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}



def f(steps, cur_col=0, solution_tracker=1):
    for (x,y), distance in steps:
        cur_col += x*distance
        solution_tracker += y*distance * cur_col + distance/2

    return int(solution_tracker)

print(f((mapping[direction], int(distance)) for direction, distance, _ in dig_plan))
print(f((mapping[hexa[7]], int(hexa[2:7], 16)) for _,_,hexa in dig_plan))
