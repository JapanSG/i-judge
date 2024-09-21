'''Circular2'''
import math
def main():
    '''driver code'''
    MINE_CENTER_X = float(input())
    MINE_CENTER_Y = float(input())
    MINE_RADIUS = float(input())
    FRIEND_CENTER_X = float(input())
    FRIEND_CENTER_Y = float(input())
    FRIEND_RADIUS = float(input())
    distance = math.sqrt(((MINE_CENTER_X-FRIEND_CENTER_X)**2)+((MINE_CENTER_Y-FRIEND_CENTER_Y)**2))
    if distance < MINE_RADIUS+FRIEND_RADIUS:
        print("Yes")
    else:
        print("No")
main()
