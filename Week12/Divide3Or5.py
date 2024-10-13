'''Divide3Or5'''
def torf(n:int) -> int:
    '''sum of number that can divide by 3 or 5'''
    total = 0
    for i in range(1,n+1):
        remainder = min(i%3,i%5)
        if not remainder:
            total += i
    return total
def main():
    '''Driver Code'''
    n = int(input())
    print(torf(n))
if __name__ == "__main__":
    main()
