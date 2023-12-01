from pprint import pprint

inp = [x for x in open("i15").read().split("\n") if x]

data = inp[0].split(',')

boxes = {x: {} for x in range(256)}

def unhash(label):
    box = 0
    for ch in label:
        chv = ord(ch)
        box += chv
        box *= 17
        box %= 256
    return box

# Python dicts are ordered
for label in data:
    if '-' in label:
        label = label.replace('-', '')
        box =  unhash(label)
        print(label, ' : ', box)
        if label in boxes[box]:
            boxes[box].pop(label)
    else:
        label, lens_no = label.split('=')
        box =  unhash(label)
        print(label, ' : ', box, ' ', lens_no)
        boxes[box][label] = lens_no

ans = 0
for b_no, contents in boxes.items():
    val = 0
    for i, item in enumerate(contents.items()):
        val += (b_no + 1) * (i + 1) * int(item[1])
        print(f" ({b_no} + 1) * {i+1} * {int(item[1])}")
    ans += val

print(ans)
        
print(boxes[3])
