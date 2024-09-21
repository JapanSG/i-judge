'''RockPaperScissor'''
def main():
    '''Driver Code'''
    string = input()
    a_score = 0
    b_score = 0
    for i in range(0,len(string),2):
        a = string[i]
        b = string[i+1]
        if a == "R":
            if b == "P":
                b_score += 1
            elif b == "S":
                a_score += 1
        elif a == "P":
            if b == "R":
                a_score += 1
            elif b == "S":
                b_score +=1
        else:
            if b == "R":
                b_score += 1
            elif b == "P":
                a_score += 1
    if a_score > b_score:
        print(f"A win {a_score}-{b_score}")
    elif a_score < b_score:
        print(f"B win {b_score}-{a_score}")
    else:
        print(f"DRAW {a_score}")
main()
