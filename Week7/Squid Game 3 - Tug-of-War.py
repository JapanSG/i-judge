'''Squid Game 3 - Tug-of-War'''
def main() -> None:
    '''Driver Code'''
    a_force = 0
    for _ in range(10):
        a_force += int(input())
    b_force = 0
    for _ in range(10):
        b_force += int(input())
    if a_force > b_force:
        print("B")
    elif a_force < b_force:
        print("A")
    else:
        print("AB")
if __name__ == "__main__":
    main()
