'''Safe'''
def main():
    '''Driver Code'''
    password = input()
    key = input()
    turns = 0
    for i in zip(password,key):
        diff = abs(ord(i[0])-ord(i[1]))
        turns += min(diff,26-diff)
    print(turns)
if __name__ == "__main__":
    main()
