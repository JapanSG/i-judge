'''Impostor'''
import json
def main():
    '''Driver Code'''
    players = {}
    dead = {}
    while True:
        jsonstr = input()
        if jsonstr == "Start":
            break
        player = json.loads(jsonstr)
        players.update(player)
    while True:
        ejected = input()
        if ejected == "End":
            break
        dead[ejected] = players.pop(ejected)
    impostor_num = list(players.values()).count("Impostor")
    print(f"{impostor_num} Impostor Remains")
    print("***Alive***")
    for player in sorted(players):
        print(f"{player} : {players[player]}")
    print("***Dead***")
    for ghost in sorted(dead):
        print(f"{ghost} : {dead[ghost]}")
if __name__ == "__main__":
    main()
