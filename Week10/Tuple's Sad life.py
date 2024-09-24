'''Tuple's Sad life'''
def main():
    '''Driver Code'''
    arr = input().split()
    val = input()
    for _ in range(arr.count(val)):
        print((f"{arr.index(val)} "*arr.count(val)).strip())
if __name__ == "__main__":
    main()
