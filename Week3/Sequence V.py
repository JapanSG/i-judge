'''Sequence V'''
import math
def main():
    """Sequence V"""
    x = int(input())
    for i in range(0 , math.ceil(x/7)):
        for j in range(x-7*(i) , (x-7)-7*i , -1):
            if j <= 0:
                break
            print(j, end = " ")
        print("")
main()
