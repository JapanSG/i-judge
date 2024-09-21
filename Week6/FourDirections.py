'''FourDirections'''
def directions(char,level):
    '''print directions based on the level and char'''
    if char == "U":
        if level == 1:
            print(" *** ",end = " ")
        elif level == 2:
            print("* * *",end = " ")
        else:
            print("  *  ",end = " ")
    elif char == "D":
        if level == 2:
            print("* * *",end = " ")
        elif level == 3:
            print(" *** ",end = " ")
        else:
            print("  *  ",end = " ")
    elif char == "L":
        if not level or level ==4:
            print("  *  ",end = " ")
        elif level in (1,3):
            print(" *   ",end = " ")
        else:
            print("*****",end = " ")
    else:
        if not level or level == 4:
            print("  *  ",end = " ")
        elif level in (1,3):
            print("   * ",end = " ")
        else:
            print("*****",end = " ")

def main():
    '''Driver Code'''
    direction = input()
    for level in range(5):
        for char in direction:
            directions(char,level)
        print("")
main()
