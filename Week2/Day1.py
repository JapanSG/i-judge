'''Day1'''
def main():
    '''driver code'''
    YEAR = int(input())
    if YEAR%4:
        print("No")
    else:
        if YEAR%100:
            print("Yes")
        else:
            if YEAR%400:
                print("No")
            else:
                print("Yes")
main()
