'''Pringles'''
def main():
    '''Driver Code'''
    top = input()
    chips = input()
    bottom = input()
    finger = int(input())
    total = 0
    for i in range(len(top)):
        if finger < i+1:
            break
        if chips[i] == ")":
            chips = chips[:i]+" "+chips[i+1:]
            total += 1
    print(total)
    if ")" in chips:
        print("There are still some left.")
    else:
        print("None.")
    print(top)
    print(chips)
    print(bottom)
main()
