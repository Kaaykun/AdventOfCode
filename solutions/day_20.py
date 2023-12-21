from collections import deque
import math

class Module:
    def __init__(self, line: str) -> None:
        # Example line: %gv -> lq, pm
        typename, outputs = line.strip().split(' -> ')

        if typename == 'broadcaster':
            self.type = 'b'
            self.name = typename
            self.memory = None
        elif typename[0] == '%':
            self.type = 'f'
            self.name = typename[1:]
            self.memory = 0
        elif typename[0] == '&':
            self.type = 'c'
            self.name = typename[1:]
            self.memory = {}
        else:
            assert False

        self.outputs = outputs.split(', ')

    def __repr__(self) -> str:
        return f'<Module {self.name} {[self.type]}: {self.outputs}>'

class System:
    def __init__(self, lines: list[str]) -> None:
        self.hi = 0
        self.lo = 0
        self.modules = {}

        for line in lines:
            module = Module(line)
            self.modules[module.name] = module

        for module in self.modules.values():
            for output in module.outputs:
                if output not in self.modules:
                    continue

                output_module = self.modules[output]

                if output_module.type == 'c':
                    output_module.memory[module.name] = 0

    def push(self, n=None, key_modules=None) -> None:
        i = 1

        while True:
            # State: (source, hi/lo, destination)
            queue = deque([('button', 0, 'broadcaster')])

            while queue:
                source, pulse, dest_name = queue.popleft()

                if pulse == 0:
                    self.lo += 1
                else:
                    self.hi += 1

                if key_modules and source in key_modules and pulse == 1:
                    # print(f'Sending {pulse} from {source} to {dest_name} at push {i}')
                    if not key_modules[source]:
                        key_modules[source] = i
                    if all(key_modules.values()):
                        return

                if dest_name not in self.modules:
                    continue

                module = self.modules[dest_name]
                if module.type == 'b':
                    next_pulse = pulse
                elif module.type == 'f':
                    if pulse == 1:
                        continue
                    module.memory = int(not module.memory)
                    next_pulse = module.memory
                elif module.type == 'c':
                        module.memory[source] = pulse
                        next_pulse = 0 if all(module.memory.values()) else 1

                for output in module.outputs:
                    queue.append((module.name, next_pulse, output))

            i += 1
            if n and i > n:
                return


with open('data/day_20.txt', 'r') as file:
    lines = file.readlines()

### PART 1 ###
system1 = System(lines)
system1.push(n=1000)

part1 = system1.lo * system1.hi
print(f'Part 1: {part1}')

### PART 2 ###
system2 = System(lines)

for module in system2.modules.values():
    if 'rx' in module.outputs:
        # print(f'Found module that feeds rx: {module.name}')
        to_rx = module

key_modules = {}

for module in system2.modules.values():
    if to_rx.name in module.outputs:
        # print(f'Found {module.name} inputs to {to_rx.name}: {module}')
        key_modules[module.name] = None

system2.push(key_modules=key_modules)
part2 = math.lcm(*key_modules.values())
print(f'Part 2: {part2}')
