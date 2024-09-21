'''BrickBridge'''
def bridge(small,big,goal):
    '''driver code'''
    numberOfBig = goal//5
    length = 5*min(big,numberOfBig)
    if goal-length > small:
        print(-1)
    else:
        print(goal-length)
bridge(int(input()),int(input()),int(input()))
