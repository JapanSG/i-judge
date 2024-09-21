'''Sequence III'''
def main():
    '''driver code'''
    num = int(input())
    for i in range(num):
        for j in range(i+2,num+2+i):
            print(j,"",end="")
        print("")
main()
