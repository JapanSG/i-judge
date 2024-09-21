'''Stair'''
def main():
    '''Driver Code'''
    most = int(input())
    num = int(input())
    print(step(most,num))
def step(most,num):
    '''To find how many step it takes to go up to floor 2    '''
    height = 0
    totalstep = 0
    possible = True
    for _ in range(num):
        x = int(input())
        if x > most:
            possible = False
        height += x
        if height >= most:
            if height > most:
                height = x
            else:
                height = 0
            totalstep += 1
    if not possible:
        return "NO"
    if height > 0:
        return totalstep+1
    return totalstep

main()
