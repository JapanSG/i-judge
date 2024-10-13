'''Kabata'''
def is_kabata(message:str) -> bool:
    '''Check if kabata'''
    length = len(message)
    i = 0
    while i < length:
        if message[i] in "tk":
            i += 1
            if i >= length or message[i] != "a":
                return False
        elif message[i] == "b":
            i += 1
            if i >= length or message[i] != "a":
                return False
            if i == length-1:
                return True
            if message[i+1] == "k" and (message[i+2] != "k" or message[i+3] != "a") :
                return False
            if message[i+1] == "k":
                i += 3
        else:
            return False
        i += 1
    return True
def main():
    '''Driver Code'''
    num = int(input())
    for _ in range(num):
        message = input()
        if is_kabata(message):
            print("yes")
        else:
            print("no")
if __name__ == "__main__":
    main()
