'''Calculator'''
def main():
    '''Driver Code'''
    n = int(input())
    total = 0
    for i in range(1,n+1):
        total += len(str(i)) + 1
    if n == 1:
        print(1)
    else:
        print(total)
if __name__ == "__main__":
    main()
