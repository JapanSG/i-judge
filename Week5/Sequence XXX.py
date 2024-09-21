'''SequenceXXX'''
def main():
    '''Driver Code'''
    height  = int(input())
    num = int(input())
    #print the 1st row
    if height == 1:
        for _ in range(num):
            print("*",end = " ")
        return
    for _ in range(num):
        print("*"*height,end = " ")
    print("")
    #print 2nd to (height-1)/2th row
    for i in range((height-3)//2):
        for _ in range(num):
            print("*"+(" "*i)+"*"+" "*(height-(4+2*i))+"*"+(" "*i)+"*",end =" ")
        print("")
    #print the middle row((height+1)/2)
    for _ in range(num):
        print("*","*","*",sep = " "*((height-3)//2),end = " ")
    print("")
    #print middle+1 to 2nd last row
    for i in range((height-3)//2-1,-1,-1):
        for _ in range(num):
            print("*"+(" "*i)+"*"+" "*(height-(4+2*i))+"*"+(" "*i)+"*",end =" ")
        print("")
    #print the last row
    for _ in range(num):
        print("*"*height,end = " ")
    print("")
main()
