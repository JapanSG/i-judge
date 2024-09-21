'''PhoneNumber'''
def main():
    '''Driver Code'''
    num = input()
    cat = input()
    string = f"{num[-1:-5:-1]} {num[-5:-9:-1]} {num[-9::-1]}"[::-1]
    if cat == "International":
        string = "+66"+string[1:]
    print(string.strip())
main()
