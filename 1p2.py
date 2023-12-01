inp = [x for x in open("i1").read().split("\n")]


nums = {"nine": 9, "eight": 8, "two": 2,  "one": 1, "three": 3,
        "four": 4, "five": 5, "six": 6, 
        "seven": 7}

def findnums(line):
    for num in nums:
        if line.find(num) != -1: 
            return True, nums[num]
    return False, ''

val = 0
for u, d in enumerate(inp):

    if not d: continue
    firstnum = ''
    found = False
    while not found:
        for q in range(len(d)+1):
            string = d[0:q]
            for c in string:
                if c.isnumeric():
                    found = True
                    firstnum = c
                    break
            if not found:
                found, firstnum = findnums(string)
                if found: break


    lastnum = ''
    found = False
    while not found:
        for q in range(len(d)+1):
            string = d[len(d)-q:]
            for c in string[::-1]:
                if c.isnumeric():
                    found = True
                    lastnum = c
                    break
            if not found:
                found, lastnum = findnums(string)
                if found: break


    print(d)
    print(f"first: {firstnum}\nlast: {lastnum}")
    val += int(f"{firstnum}{lastnum}")

    
print(val)

