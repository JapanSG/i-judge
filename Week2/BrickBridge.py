'''BrickBridge'''
def main():
    '''driver code'''
    small = int(input())
    big = int(input())
    goal = int(input())
    numberOfBig = goal//5
    length = 0
    if numberOfBig > big:
        length = big*5
    else:
        length = numberOfBig*5
    numberOfSmall = goal-length
    if numberOfSmall > small:
        print(-1)
    else:
        print(numberOfSmall)
main()
