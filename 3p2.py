from pprint import pprint 
from collections import Counter, defaultdict

inp = [x for x in open("i3").read().split("\n")]

data = []
mask = []
for i, line in enumerate(inp):
    if not line: continue
    data.append([x for x in line])
    mask.append([0 for _ in line])

diff_chars = []



# make a dict of key = gear loc val = num locs adjacent
gears = defaultdict(list)
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        valid = 0
        for dir in [(0, 0), (-1, -1), (-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]:
            x = i+dir[0]
            y = j+dir[1]
            if x < 0: continue
            if y < 0: continue
            try:
                ch_2 = data[x][y]
            except:
                ch_2 = '.'
            if ch_2 == '*' and ch.isdigit():
                gears[(x, y)].append((i, j))
        mask[i][j] += valid 

def get_connected_gear(loc):
    for gloc, nlocs in gears.items():
        if loc in nlocs:
            return gloc
    return None

gear_nums = defaultdict(list) 
for i, line in enumerate(data):
    line_nums = []
    current_num = ''
    gloc = None
    for j, ch in enumerate(line):
        print(f"{ch} on {i} gloc: {gloc}")
        if i == 7 and j == 8: pass
        if j == 0 and ch.isdigit():
            current_num = ch
            gloc = get_connected_gear((i, j))
        elif ch.isdigit():
            current_num += ch
            if gloc is None:
                gloc = get_connected_gear((i, j))
            if j == len(line)-1 and gloc:
                print(f"Adding {current_num} to {gloc}")
                gear_nums[gloc].append(int(current_num))
        else:
            if gloc:
                print(f"Adding {current_num} to {gloc}")
                gear_nums[gloc].append(int(current_num))
            current_num = ''
            gloc = None

val = 0
for gloc, nums in gear_nums.items():
    if len(nums) == 2:
        val += (nums[0] * nums[1])

print(val)


