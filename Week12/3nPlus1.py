'''3nPlus1'''
MEMO = {
    1:1
}
def f(num:int,times:int) -> int:
    '''3n+1 series recursion find how many memeber is in the given number series'''
    if num in MEMO:
        return times + MEMO[1]
    if not num%2:
        return f(num/2, times + 1)
    return f(3*num+1, times + 1)
def main():
    '''Driver Code'''
    while True:
        num = int(input())
        if not num:
            break
        print(f(num,0))
if __name__ == "__main__":
    main()
