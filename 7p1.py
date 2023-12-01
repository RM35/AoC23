from collections import Counter

inp = [x for x in open("i7").read().split("\n")]

O = '23456789TJQKA'

draws = ["FIVE", "FULL", "FOUR", "2PAIR", "THREE", "TWO", "HIGH"]
draws = draws[::-1]

e = {"2": "A",
     "3": "B",
     "4": "C",
     "5": "D",
     "6": "E",
     "7": "F",
     "8": "G",
     "9": "H",
     "T": "I",
     "J": "J",
     "Q": "L",
     "K": "M",
     "A": "N"}

def draw_score(cards):
    val = 1

    value = ""
    for c in cards:
        value += e[c]
    
    return value

data = []
i = 0
for line in inp:
    print(f"{i}: {line}")
    i+=1
    if not line: continue
    cards = line.split()[0]
    bids = int(line.split()[1])

    counts = Counter(cards)
    if len(counts) == 1:
        # Five of kind
        print(f"FIVE OF KIND {i}")
        data.append((7, draw_score(cards), bids, cards))
    if len(counts) == 2:
        cs = counts.items()
        for card, count in cs:
            if count == 4:
                # 4 of kind
                print(f"FOUR OF KIND {i}")
                data.append((6, draw_score(cards), bids, cards))
                break
            if count == 3:
                # Full house
                print(f"FULL HOUSE {i}")
                data.append((5, draw_score(cards), bids, cards))
                break
    if len(counts) == 3:
        cs = counts.items()
        for card, count in cs:
            if count == 3:
                # 3 of kind
                print(f"THREE {i}")
                data.append((4, draw_score(cards), bids, cards))
                break
            if count == 2:
                # 2 Pairs
                print(f"2 PAIR {i}")
                data.append((3, draw_score(cards), bids, cards))
                break
    if len(counts) == 4:
        cs = counts.items()
        for card, count in cs:
            if count == 2:
                # 2 of kind
                print(f"TWO  {i}")
                data.append((2, draw_score(cards), bids, cards))
                break
    if len(counts) == 5:
        # High card
        print(f"HIGH CARD  {i}")
        data.append((0, draw_score(cards), bids, cards))

data.sort(reverse=False, key=lambda x: (x[0], x[1]))
ans = 0
for i, line in enumerate(data):
    rank = i+1
    bid  = line[2]
    draw = line[0]
    cards = line[3]
    draw_val = line[1]
    ans += (rank*bid)
   #  print(f"{rank=} {line[0]} {bid=} {cards=} {draws[draw]} {draw_val}")


print(len(data))
print(ans)
