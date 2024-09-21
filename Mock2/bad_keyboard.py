'''bad_keyboard'''
def main():
    '''Driver Code'''
    message = input()
    fixed = ""
    for i in message:
        if i == "i":
            fixed += "o"
        elif i == "o":
            fixed += "i"
        elif i == "I":
            fixed += "O"
        elif i == "O":
            fixed += "I"
        else:
            fixed += i
    print(fixed)
main()
