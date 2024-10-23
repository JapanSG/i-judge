'''Supercar Parking'''
def main():
    '''Driver Code'''
    space = list(input())
    length = len(space)
    total = 0
    if length == 1 and space[0] == "0":
        print(1)
        return
    for i in range(length):
        if space[i] == "1":
            continue
        if not i and i + 1 < length and space[i+1] == "0":
            total += 1
            space[i] = 1
        elif i == length-1 and i - 1 > -1 and space[i-1] == "0":
            total += 1
            space[i] = 1
        elif i+1 < length and i-1 > -1 and space[i-1] == "0" and space[i+1] == "0":
            total += 1
            space[i] = 1
    print(total)
main()
