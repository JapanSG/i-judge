'''US Interstate Number System'''
def main():
    '''Driver Code'''
    number = input()
    if int(number[-2:]) < 5 or int(number[-2:]) > 95:
        print("Others")
        return
    if len(number) == 3:
        if not number[-1] in ("0","5"):
            print("Others")
        else:
            if not int(number[0])%2:
                print("Even Minor Interstate")
            else:
                print("Odd Minor Interstate")
            print(f"I-{int(number[1:])}")
    elif len(number) in (1,2):
        if number[-1] == "0":
            print("Horizontal Major Interstate")
            print(f"I-{int(number)}")
        elif number[-1] == "5":
            print("Vertical Major Interstate")
            print(f"I-{int(number)}")
        else:
            print("Others")
    else:
        print("Others")
if __name__ == "__main__":
    main()
