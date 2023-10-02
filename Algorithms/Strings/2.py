import itertools

def winnerOfGame(colors: str) -> bool:
    winner_a = False
    for gamer in itertools.cycle(["A", "B"]):
        if "".join([gamer]*3) in colors:
            colors = colors.replace("".join([gamer]*3), "".join([gamer]*2), 1)
            winner_a = not winner_a
        else:
            break
    return winner_a

colors = "AAABABB"
print(winnerOfGame(colors))

colors = "AA"
print(winnerOfGame(colors))

colors = "ABBBBBBBAAA"
print(winnerOfGame(colors))