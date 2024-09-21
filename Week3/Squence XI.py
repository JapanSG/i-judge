'''Squence XI'''
def main():
    '''driver code'''
    num = int(input())
    #print the top half
    for i in range(1,num):
        for j in range(1,i+1):
            print(f"{j:02d}",end = " ")
        while j < num-1:
            print(f"{i:02d}",end = " ")
            j += 1
        print(f"{i:02d}",end =" ")
        for _ in range(num-2-i+1):
            print(f"{i:02d}",end =" ")
        for k in range(i,0,-1):
            print(f"{k:02d}",end=" ")
        print("")
    #print the middle
    for i in range(1,num+1):
        print(f"{i:02d}",end =" ")
    for i in range(num-1,0,-1):
        print(f"{i:02d}",end =" ")
    print("")
    #print the bottom half
    for i in range(num-1,0,-1):
        for j in range(1,i+1):
            print(f"{j:02d}",end = " ")
        while j < num-1:
            print(f"{i:02d}",end = " ")
            j += 1
        print(f"{i:02d}",end =" ")
        for _ in range(num-2-i+1):
            print(f"{i:02d}",end =" ")
        for k in range(i,0,-1):
            print(f"{k:02d}",end=" ")
        print("")
main()
