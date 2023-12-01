inp = [x for x in open("i1").read().split("\n")]

val = 0
for d in inp:
    j = []
    for i, c in enumerate(d):
        if c.isnumeric():
            j.append(c)

    if len(j) == 1:
        val += int(f"{j[0]}{j[0]}")
    if len(j) > 1:
        val += int(f"{j[0]}{j[-1]}") 
    
print(val)

