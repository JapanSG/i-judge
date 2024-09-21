'''Sequence X'''
def main():
    '''Driver Code'''
    num = int(input())
    for i in range(1,num+1):
        print("   "*(num-i),end = "")
        for k in range(1,i+1):
            print(f"{k:02d}",end = " ")
        for l in range(i-1,0,-1):
            print(f"{l:02d}",end = " ")
        print("")
    for j in range(num-1,0,-1):
        print("   "*(num-j),end = "")
        for k in range(1,j+1):
            print(f"{k:02d}",end = " ")
        for l in range(j-1,0,-1):
            print(f"{l:02d}",end = " ")
        print("")
main()
