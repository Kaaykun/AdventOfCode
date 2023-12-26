def get_input():
    file_path = 'data/day_01.txt'

    with open(file_path, 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.strip() for line in input_lines]

    return input_lines

def part1():
    def get_digits():
        numeric_digits = []
        input_lines = get_input()

        for line in input_lines:
            digits = ''.join(filter(str.isdigit, line))
            if digits:
                numeric_digits.append(digits)

        return numeric_digits


    def calibrate_values():
        numeric_digits = get_digits()
        calibration_values = []

        for number in numeric_digits:
            if len(number) == 1:
                calibration_values.append(int(number * 2))
            elif len(number) > 2:
                number = number[0] + number[-1]
                calibration_values.append(int(number))
            else:
                calibration_values.append(int(number))

        return calibration_values

    calibration_values = calibrate_values()
    return (sum(digit for digit in calibration_values))


def part2():
    str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def get_results():
        results = []

        input_lines = get_input()
        for line in input_lines:
            temp = []
            i = 0

            while i < len(line):
                if line[i].isdigit():
                    temp.append(line[i])
                    i += 1
                else:
                    for c in str_digits:
                        if c in line[i:i + len(c)]:
                            temp.append(str(str_digits.index(c)))
                            i += 1
                            break
                    else:
                        i += 1

            results.append(temp)
        return results

    def calculate():
        calculations = []

        results = get_results()
        for line in results:
            first = line[0]
            last = line[-1]
            total = int(first + last)

            calculations.append(total)

        return(sum(calculations))

    return(calculate())

print(part1())
print(part2())
