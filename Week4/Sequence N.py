'''Sequence N'''
def main():
    '''Driver Code'''
    num = int(input())
    for i in range(1,num+1):
        print("*",end = "")
        for _ in range(i-2):
            print(" ",end="")
        if i not in [1,num]:
            print("*",end="")
        for _ in range(num-i-1):
            print(" ",end="")
        print("*")
main()
