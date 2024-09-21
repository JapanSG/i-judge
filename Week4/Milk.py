'''Milk'''
def main():
    '''Driver Code'''
    cost = int(input())
    pro = int(input())
    free = int(input())
    money = int(input())
    bottle = money//cost
    cap = bottle
    if pro > 0:
        while cap >= pro:
            used = (cap//pro)*pro
            bonus = (cap//pro)*free
            cap -= used
            bottle += bonus
            cap += bonus
    print(int(bottle))
main()
