'''Circular1'''
import math
def main():
    '''driver code'''
    H = float(input())
    K = float(input())
    R = float(input())
    X = float(input())
    Y = float(input())
    d = math.sqrt(((H-X)**2)+((K-Y)**2))
    if d > R :
        print("No")
    else:
        print("Yes")
main()
