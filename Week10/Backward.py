'''Backward'''
def main():
    '''Driver Code'''
    lis = []
    while True:
        val = input()
        if val == "NULL":
            break
        lis.append(val)
    lis.reverse()
    for val in lis:
        print(val)
if __name__ == "__main__":
    main()
