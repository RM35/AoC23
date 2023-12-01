inp = [x for x in open("i4").read().split("\n")]

# Runs slow. might have been saved by the M2 haha
data = []
for line in inp:
    if not line: continue
    line = line.replace("  ", " ")
    nums = line.split(": ")[1].split(" | ")
    winners = [int(n) for n in nums[0].split()]
    chose = [int(n) for n in nums[1].split()]
    data.append((winners, chose))

ans = 0
game_scores = [[0, 1] for _ in range(len(data))] 
game = 0 
to_eval = [1 for _ in range(len(data))]
s_count = [] 
for win, nums in data: 
    print(f"{game}: {to_eval[game]}")
    s_count.append(to_eval[game])

    while to_eval[game] > 0:
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
        # print(f"{win} | {nums} : {score}")
        for x in range(j):
            to_eval[game+x+1] += 1
        ans += score
        to_eval[game] -= 1
    game += 1
            
ans = 0
for num in s_count:
    ans += num
print(ans)

    
