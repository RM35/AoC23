from pprint import pprint
inp = [x for x in open("i8").read().split("\n\n")]

dirs = inp[0].strip()

G = {}
for node in inp[1].split('\n'):
    if not node: continue
    loc = node.split(" = ")[0] 
    con = node.split("(")[1].split(")")[0].split(", ")
    G[loc] = con


current_node = 'AAA'
i = 0
while current_node != 'ZZZ':
    d = dirs[i%len(dirs)]
    print(f"LOC: {current_node} : {G[current_node]}")
    if d == 'L':
        print("GO LEFT")
        current_node = G[current_node][0]
    else:
        print("GO RIGHT")
        current_node = G[current_node][1]
    i += 1 
    print(current_node)

print(i)


