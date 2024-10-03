'''WordSequence I'''
def main():
    '''Driver Code'''
    message = input()
    length = len(message)
    for i in range(length):
        print(message[:i+1])
if __name__ == "__main__":
    main()
