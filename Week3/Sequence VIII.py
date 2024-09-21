'''Sequence VIII'''
def main():
    '''Driver Code'''
    num = int(input())
    for i in range(1,num+1):
        print("   "*(num-i),end = "")
        for k in range(1,i+1):
            print(f"{k:02d}",end = " ")
        print("")
main()
