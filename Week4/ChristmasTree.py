'''ChristmasTree'''
def main():
    '''Driver Code'''
    leaf = int(input())
    stem = int(input())
    for i in range(1,leaf+1):
        # if leaf == 1:
        #     leaf = 2
        print(" "*(leaf-i),"*"*(2*i-1)," "*(leaf-i),sep = "")
    for _ in range(stem):
        print(" "*(leaf-2),"---",sep = "")
main()
