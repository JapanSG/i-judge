'''Sequence VII'''
def main():
    '''Driver Code'''
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print("")
    for k in range(num-1,0,-1):
        for l in range (1,k+1):
            print(l,end = " ")
        print("")
main()
