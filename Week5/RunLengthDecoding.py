'''Run Length Decoding'''
def main():
    '''Driver Code'''
    key = input()
    length = len(key)
    i = 0
    while i < length:
        num = ""
        while key[i].isdigit():
            num += key[i]
            i += 1
        print(key[i]*int(num),end ="")
        i+=1
main()
