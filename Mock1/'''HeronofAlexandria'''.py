'''HeronofAlexandria'''
import math
def main():
    '''Driver Code'''
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a+b+c)/2
    print(f"{math.sqrt(s*(s-a)*(s-b)*(s-c)):.3f}")
main()
