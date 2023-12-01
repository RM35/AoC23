from pprint import pprint 
from collections import Counter

inp = [x for x in open("i3").read().split("\n")]

data = []
mask = []
for i, line in enumerate(inp):
    if not line: continue
    data.append([x for x in line])
    mask.append([0 for _ in line])

diff_chars = []

for i, line in enumerate(data):
    for j, ch in enumerate(line):
        if mask[i][j] ==  1: continue
        diff_chars.append(ch)
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
            if ch_2 != '.' and not ch_2.isdigit():
                valid = 1
        mask[i][j] = valid 

if False:
    chars = Counter(diff_chars)
    print(chars.most_common())


valid_num_data = []
for i, line in enumerate(data):
    line_nums = []
    current_num = ''
    valid_num = False
    for j, ch in enumerate(line):
        if j == 0 and ch.isdigit():
            current_num = ch
            if bool(mask[i][j]):
                valid_num = True
        elif ch.isdigit():
            current_num += ch
            if bool(mask[i][j]):
                valid_num = True
            if j == len(line)-1 and valid_num:
                line_nums.append(int(current_num))
        else:
            if valid_num:
                line_nums.append(int(current_num))
            current_num = ''
            valid_num = False

    if True:
        print(i)
        try:
            print("".join(x for x in data[i-1]))
        except:
            pass
        print("".join(x for x in data[i]))
        try:
            print("".join(x for x in data[i+1]))
        except:
            pass
        print(line_nums)
        print("\n")
    valid_num_data.append(line_nums)


sum = 0
for i, line in enumerate(valid_num_data):
    print(line)
    for num in line:
        sum += num

print(sum)


