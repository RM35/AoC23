from pprint import pprint

inp = [x for x in open("i2").read().split("\n")]


data = []
games = [] 
i = 0
for line in inp:
    if not line: continue
    games = line.split(": ")[1].replace(",", "").split("; ")
    games_rounds = []
    for game in games:
        cols_in_game = {}
        for col in ["red", "green", "blue"]:
            if col in game:
                cols_in_game[col] = int(game.split(col)[0].split()[-1])
        games_rounds.append(cols_in_game)
    data.append(games_rounds)

config = {"red": 12, "green": 13, "blue": 14}

sum = 0
for i, game in enumerate(data):
    game_possible = True
    for round in game:
        for col, val in round.items():
            if val > config[col]:
                game_possible = False
    if game_possible:
        sum += i+1

print(sum)
