'''Easy Histogram'''
def main():
    '''Driver Code'''
    message = input()
    dct = {}
    for char in message:
        if char.isalpha():
            dct[char] = dct.get(char,0) + 1
    for key in sorted(dct,key = lambda a:(a.lower(),a.swapcase())):
        print(f"{key} = {dct[key]}")
if __name__ == "__main__":
    main()
