from functools import reduce  # Required in Python 3
import operator

lines = []
with open("input") as f:
    lines = [l for l in f]

#part1 races = zip([int(t) for t in lines[0].split(':')[1].strip().split()], [int(t) for t in lines[1].split(':')[1].strip().split()])
races = zip([int(''.join(lines[0].split(':')[1].strip().split()))], [int(''.join(lines[1].split(':')[1].strip().split()))])
print(reduce(operator.mul, [len([i for i in range(t) if (t - i) * i > d]) for t, d in races], 1))