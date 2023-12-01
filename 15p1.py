inp = [x for x in open("i15").read().split("\n") if x]

data = inp[0].split(',')

ans = 0
for code in data:
    val = 0
    for ch in code:
        chv = ord(ch)
        val += chv
        val *= 17
        val %= 256
    ans += val

print(ans)
