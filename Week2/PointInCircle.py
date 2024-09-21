'''PointInCircle'''
import math
def main():
    '''driver code'''
    H = int(input())
    K = int(input())
    R = int(input())
    X = int(input())
    Y = int(input())
    d = math.sqrt(((H-X)**2)+((K-Y)**2))
    if d > R :
        print(False)
    else:
        print(True)
main()
