import sys

lines = []
with open("input") as f:
    lines = [l for l in f]

seeds = [int(a) for a in lines[0].split(':')[1].strip().split()]
seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
maps = [[[int(i) for i in l.split()] for l in map.split('\n')[1:]] for map in ''.join(lines[1:]).split("\n\n")]
print(maps)
local_mins = []
for map in maps:
    new_seed_ranges = []
    for seed_range in seed_ranges:
        for d, s, r in map:
            if seed_range[0] >= s and seed_range[0] < s + r:
                if seed_range[0] + seed_range[1] < s + r:
                    new_seed_ranges.append((d + seed_range[0] - s, seed_range[1]))
                    break
                else:
                    new_seed_ranges.append((d + seed_range[0] - s, s + r - seed_range[0]))
                    seed_range = (s + r, seed_range[1] - s - r + seed_range[0])
            elif seed_range[0] + seed_range[1] >= s and seed_range[0] + seed_range[1] < s + r:
                new_seed_ranges.append((s, seed_range[0] + seed_range[1] - s))
                seed_range = ((seed_range[0], s - seed_range[0]))                
        else:
            new_seed_ranges.append(seed_range)
    seed_ranges = new_seed_ranges

print(min([a for a, b in seed_ranges]))