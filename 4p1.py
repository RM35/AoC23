
inp = [x for x in open("i4").read().split("\n")]

data = []
for line in inp:
    if not line: continue
    line = line.replace("  ", " ")
    nums = line.split(": ")[1].split(" | ")
    winners = [int(n) for n in nums[0].split()]
    chose = [int(n) for n in nums[1].split()]
    data.append((winners, chose))

ans = 0
for win, nums in data: 
    score = 0
    j = 0
    for i, wn in enumerate(win):
        if wn in nums:
            if j == 0:
                score = 1
                j+=1
            else:
                score *=2
                j+=1
    print(f"{win} | {nums} : {score}")
    ans += score
            
print(ans)

    
