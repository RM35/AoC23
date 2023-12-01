from pprint import pprint
from functools import lru_cache
import random

inp = [x for x in open("i5").read().split("\n\n")]

seeds = []
ssmap = []
sfmap = []
fwmap = []
wlmap = []
ltmap = []
thmap = []
hlmap = []


seedr = [int(x) for x in inp[0].split("seeds: ")[1].split()]
seeds = []

for i in range(0, len(seedr)-1, 2):
    seeds.append((seedr[i], seedr[i+1]))


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

ssmap.sort(key=lambda x: x[0])
sfmap.sort(key=lambda x: x[0])
fwmap.sort(key=lambda x: x[0])
wlmap.sort(key=lambda x: x[0])
ltmap.sort(key=lambda x: x[0])
thmap.sort(key=lambda x: x[0])
hlmap.sort(key=lambda x: x[0])

maps = [ssmap, sfmap, fwmap, wlmap, ltmap, thmap, hlmap]


ssmap = ssmap 
for i,x in enumerate(ssmap):
    ssmap[i][0] /= 100000000
    ssmap[i][1] /= 100000000
    ssmap[i][2] /= 100000000
    ssmap[i][0] = round(ssmap[i][0], 1)
    ssmap[i][1] = round(ssmap[i][1], 1)
    ssmap[i][2] = round(ssmap[i][2], 1)

pprint(ssmap)
exit()

@lru_cache(maxsize=None)
def get_newloc(val, map_i):
    for m in maps[map_i]:
        if m[1] <= val and val < m[1]+m[2]:
            offset = val-m[1]
            if map_i == 6:
                return m[0]+offset
            return get_newloc(m[0]+offset, map_i+1)
    offset = val-m[1]
    if map_i == 6:
        return val 
    return get_newloc(val, map_i+1)

for i in range(1):

    sr = []
    # Approx seed for lowest on initial broad run
    app = 3283842679
    # Check around this number check for converging
    ran = 1000000
    for x in range(ran):
        sr.append(int(app+(ran/2)-x))

    if False:
        sr = []
        for s, r in seeds:
            for f in range(0, r, 200000):
                sr.append(s+f)

    lowest = 999999999999999999999999
    for seed in sr:
        loc = get_newloc(seed, 0)
        if loc < lowest:
            # print(f"LOW SEED: {seed}")
            print(loc)
            lowest = loc




