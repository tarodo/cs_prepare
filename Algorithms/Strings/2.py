import itertools

def winnerOfGame(colors: str) -> bool:
    cur_el = colors[0]
    cur_ok = 1
    count_a = count_b = 0
    for idx in range(1, len(colors)):
        if colors[idx] == cur_el:
            cur_ok += 1
        else:
            cur_el = colors[idx]
            cur_ok = 1
        if cur_ok >= 3:
            if cur_el == "A":
                count_a += 1
            else:
                count_b += 1
    return count_a > count_b


colors = "AAABABB"
print(winnerOfGame(colors))

colors = "AA"
print(winnerOfGame(colors))

colors = "ABBBBBBBAAA"
print(winnerOfGame(colors))