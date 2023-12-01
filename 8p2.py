from pprint import pprint
inp = [x for x in open("i8").read().split("\n\n")]

dirs = inp[0].strip()

G = {}
for node in inp[1].split('\n'):
    if not node: continue
    loc = node.split(" = ")[0] 
    con = node.split("(")[1].split(")")[0].split(", ")
    G[loc] = con


cur_nodes = []
for no in G.keys():
    if no.endswith("A"):
        cur_nodes.append(no)

def finished():
    for no in cur_nodes:
        if no[-1] != 'Z':
            return False
    print(cur_nodes)
    return True

def next_z(start, d):
    i = 0
    current_node = start
    while not current_node.endswith('Z'):
        d = dirs[i%len(dirs)]
        if d == 'L':
            current_node = G[current_node][0]
        else:
            current_node = G[current_node][1]
        i += 1
    return i

for node in cur_nodes:
    print(next_z(node, 0))

# Some meta solving. used online LCM calculator

print(cur_nodes)
print(i)


