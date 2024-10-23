'''Snake'''
import json
def snake(pos:int) -> int:
    '''snake location'''
    if pos == 17:
        return 13
    if pos == 52:
        return 29
    if pos == 57:
        return 40
    if pos == 62:
        return 22
    if pos == 88:
        return 18
    if pos == 95:
        return 51
    if pos == 97:
        return 79
    return pos
def ladder(pos:int) -> int:
    '''ladder location'''
    if pos == 3:
        return 21
    if pos == 8:
        return 30
    if pos == 28:
        return 84
    if pos == 58:
        return 77
    if pos == 75:
        return 86
    if pos == 80:
        return 100
    if pos == 90:
        return 91
    return pos
def main():
    '''Driver Code'''
    num = int(input())
    rolls = json.loads(input())
    pos = {}
    players = [i for i in range(1,num+1)]
    winner = []
    for i in range(1,num+1):
        pos[i] = 1
    pointer = 0
    for i in rolls:
        pos[players[pointer]] += i
        pos[players[pointer]] = snake(ladder(pos[players[pointer]]))
        if pos[players[pointer]] >= 100:
            winner.append(players.pop(pointer))
            continue
        if pointer == len(players)-1:
            pointer = 0
        else:
            pointer += 1
    if not winner:
        print(-1)
    else:
        print(*winner)
    print(*sorted(pos,key = lambda x : (pos[x],x), reverse=True))
    print(pos)
main()
