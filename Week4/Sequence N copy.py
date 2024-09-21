'''Sequence N'''
def main():
    '''Driver Code'''
    num = int(input())
    for i in range(num):
        print("*",end = "")
        for j in range(1,num-1):
            if j == i:
                print("*",end = "")
            else:
                print(" ",end = "")
        print("*",end = "")
main()
