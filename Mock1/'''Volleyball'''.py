'''Volleyball'''
def check_finished(a,b,sets):
    '''Function'''
    game_point = 25
    if sets == 5:
        game_point = 15
    if a >= game_point and a > b:
        return bool(b <= a-2)
    if b >= game_point and b > a:
        return bool(a <= b-2)
    return False
def main():
    '''Driver Code'''
    score = input()
    a_score = 0
    b_score = 0
    a_set_score = 0
    b_set_score = 0
    sets = 1
    finished = False
    for i in score:
        if i == "A":
            a_score += 1
        else:
            b_score += 1
        if check_finished(a_score,b_score,sets):
            print(f"Set {sets}: A ({a_score}) | B ({b_score})")
            if a_score > b_score:
                a_set_score += 1
            else:
                b_set_score += 1
            sets += 1
            a_score = 0
            b_score = 0
        if a_set_score == 3 or b_set_score == 3 or sets > 5:
            finished = True
            break
    if finished and a_set_score < b_set_score:
        print(f"B won {b_set_score}:{a_set_score} set")
    elif finished and a_set_score > b_set_score:
        print(f"A won {a_set_score}:{b_set_score} set")
    else:
        print(f"Set {sets}: A ({a_score}) | B ({b_score})")
        print("The game has not finished yet.")
main()
