# Attempt time
# 33.000s 

# Remove win count loop with set intersection
# 12.000s 

# Memo the win count
# 4.000s

# Change to simple arithmetic instead of looping.
# 0.004s

# Tidy up. Remove memo, remove unsused
# 0.002s
 
inp = [x for x in open("i4").read().split("\n")]

data = []
for line in inp:
    if not line: continue
    line = line.replace("  ", " ")
    nums = line.split(": ")[1].split(" | ")
    winners = [int(n) for n in nums[0].split()]
    chose = [int(n) for n in nums[1].split()]
    data.append((winners, chose))

to_eval = [1 for _ in range(len(data))]
ans = 0
for game, vals in enumerate(data): 
    ans += to_eval[game]
    matches = len(set(vals[0]) & set(vals[1]))

    for i in range(matches):
        to_eval[game+i+1] += to_eval[game]
            
print(ans)
