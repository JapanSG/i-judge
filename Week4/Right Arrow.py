'''Right Arrow'''
def main():
    '''Driver Code'''
    width = int(input())
    height = int(input())
    for i in range(height//2):
        print(" "*i,"*"*width,sep = "")
    for i in range(height//2,-1,-1):
        print(" "*i,"*"*width,sep = "")
main()
