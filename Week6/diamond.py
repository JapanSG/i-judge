'''diamond'''
def main():
    '''Driver Code'''
    height = int(input())
    if height == 1:
        print("*")
    else:
        print(" "*((height-1)//2)+"*")
        for i in range((height-3)//2):
            print(" "*(((height-1)//2)-(i+1))+"*"+" "*(2*i+1)+"*")
        print("*"*height)
        for i in range((height-3)//2-1,-1,-1):
            print(" "*(((height-1)//2)-(i+1))+"*"+" "*(2*i+1)+"*")
        print(" "*((height-1)//2)+"*")
main()
