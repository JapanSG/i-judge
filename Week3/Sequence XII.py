'''Sequence XII'''
def main():
    '''Driver Code'''
    num = int(input())
    line = 0
    #print the top half
    for i in range(num,1,-1):
        #print first half of the line
        j = i
        while j < num:
            print(f"{j:02d}",end = " ")
            j += 1
        while j > line:
            print(f"{j:02d}",end = " ")
            j -=1
        #print ssecond half of the line12
        j += 2
        while j < num:
            print(f"{j:02d}",end = " ")
            j += 1
        print(f"{j:02d}",end = " ")
        while j > i:
            j -=1
            print(f"{j:02d}",end = " ")
        print("")
        line +=1
    #print the middle
    for i in range(1,num+1):
        print(f"{i:02d}",end = " ")
    for i in range (num-1,0,-1):
        print(f"{i:02d}",end = " ")
    print("")
    #print the bottom half
    line -=1
    for i in range(2,num+1):
        #print first half of the line
        j = i
        while j < num:
            print(f"{j:02d}",end = " ")
            j += 1
        while j > line:
            print(f"{j:02d}",end = " ")
            j -=1
        #print ssecond half of the line
        j += 2
        while j < num:
            print(f"{j:02d}",end = " ")
            j += 1
        print(f"{j:02d}",end = " ")
        while j > i:
            j -=1
            print(f"{j:02d}",end = " ")
        print("")
        line -=1
main()
