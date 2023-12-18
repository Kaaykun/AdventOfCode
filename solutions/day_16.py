g = {x+y*1j: c for y, r in enumerate(open('data/day_16.txt'))
               for x, c in enumerate(r.strip())}

def count(todo):
    done = set()
    while todo:
        p, d = todo.pop()
        while not (p,d) in done:
            done.add((p, d))
            p += d
            match g.get(p):
                case '\\': d = (d*-1j).conjugate()
                case '/':  d = (d*1j).conjugate()
                case '|':  d = 1j; todo.add((p, -1j))
                case '-':  d = 1 ; todo.add((p, -1))
                case None: break

    return len(set(x for x,_ in done)) - 1

# Part 1
print(count({(-1, 1)}))

# Part 2
print(max(map(count, ({((p-d, d))} for p in g
    for d in (1, 1j, -1, -1j) if p-d not in g))))
