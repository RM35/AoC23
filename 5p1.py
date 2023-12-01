from pprint import pprint

inp = [x for x in open("i5").read().split("\n\n")]

seeds = []
ssmap = []
sfmap = []
fwmap = []
wlmap = []
ltmap = []
thmap = []
hlmap = []

seeds = [int(x) for x in inp[0].split("seeds: ")[1].split()]
for x in inp[1].split("\n"):
    if not x: continue
    if x.startswith("seed"): continue
    ssmap.append([int(r) for r in x.split()])
for x in inp[2].split("\n"):
    if not x: continue
    if x.startswith("soil"): continue
    sfmap.append([int(r) for r in x.split()])
for x in inp[3].split("\n"):
    if not x: continue
    if x.startswith("fert"): continue
    fwmap.append([int(r) for r in x.split()])
for x in inp[4].split("\n"):
    if not x: continue
    if x.startswith("wate"): continue
    wlmap.append([int(r) for r in x.split()])
for x in inp[5].split("\n"):
    if not x: continue
    if x.startswith("ligh"): continue
    ltmap.append([int(r) for r in x.split()])
for x in inp[6].split("\n"):
    if not x: continue
    if x.startswith("temp"): continue
    thmap.append([int(r) for r in x.split()])
for x in inp[7].split("\n"):
    if not x: continue
    if x.startswith("hum"): continue
    hlmap.append([int(r) for r in x.split()])

ssmap.sort(key=lambda x: x[1])
sfmap.sort(key=lambda x: x[1])
fwmap.sort(key=lambda x: x[1])
wlmap.sort(key=lambda x: x[1])
ltmap.sort(key=lambda x: x[1])
thmap.sort(key=lambda x: x[1])
hlmap.sort(key=lambda x: x[1])

maps = [ssmap, sfmap, fwmap, wlmap, ltmap, thmap, hlmap]

def get_newloc(val, map_i):
    if val == 81: pass
    for m in maps[map_i]:
        if m[1] <= val and val < m[1]+m[2]:
            offset = val-m[1]
            if map_i == 6:
                print(f"Returning {m[0]+offset}")
                return m[0]+offset
            print(f"{val} in map {map_i} maps to {m[0]+offset}")
            return get_newloc(m[0]+offset, map_i+1)
    offset = val-m[1]
    if map_i == 6:
        print(f"Returning {val}")
        return val 
    print(f"{val} in map {map_i} maps to {val}")
    return get_newloc(val, map_i+1)

seeds_loc = {} 
for seed in seeds:
    loc = get_newloc(seed, 0)
    seeds_loc[seed] = loc

pprint(seeds_loc)
lowest = 8888888888888888888888888
for key, val in seeds_loc.items():
    if val < lowest:
        lowest = val

print(lowest)














