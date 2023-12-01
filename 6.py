inp = [x for x in open("i6").read().split("\n")]

times = [int(x) for x in inp[0].split()[1:]]
dists = [int(x) for x in inp[1].split()[1:]]

data = zip(times, dists)


def dist(t, held, rate=1):
    dist =  (t-held) * (t-held) * rate
    return dist

def held(t):
    a = 1
    b = 2*t
    c = t**2
    x = (-b + (b**2 - 4*a*c)**0.5) / 2*a
    x2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
    return max(x, x2)

races = []
for t, d in data:
    dists = []
    valid = []
    for i in range(t):
        if i % 1000 == 0 : print(i)
        race = t-i
        speed = i*1
        dist = race*speed
        dists.append((i, dist))
    for he, di in dists:
        if di > d:
            valid.append((he, di))
    races.append(valid)
    print(valid)

ans = 1
for valid in races:
    ans *= len(valid)

print(ans)



