'''FourDirections'''
def directions_1(char):
    '''helper function'''
    if char == "U":
        print(" *** ",end = " ")
    elif char == "D":
        print("  *  ",end = " ")
    elif char == "L":
        print(" *   ",end = " ")
    else:
        print("   * ",end = " ")
def directions_3(char):
    '''helper function'''
    if char == "U":
        print("  *  ",end = " ")
    elif char == "D":
        print(" *** ",end = " ")
    elif char == "L":
        print(" *   ",end = " ")
    else:
        print("   * ",end = " ")
def directions(char,level):
    '''print directions based on the level and char'''
    if level in (0,4):
        print("  *  ",end = " ")
    if level == 1:
        directions_1(char)
    if level == 2:
        if char in ("U","D"):
            print("* * *",end = " ")
        else:
            print("*****",end = " ")
    if level == 3:
        directions_3(char)
def main():
    '''Driver Code'''
    direction = input()
    for level in range(5):
        for char in direction:
            directions(char,level)
        print("")
main()
