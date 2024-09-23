'''Point Sorting'''
def printdata(data:list):
    '''print data'''
    for cord in data:
        print(f"{cord[0]} {cord[1]}")

def sort(lis:list):
    '''sort xy corordinates'''
    length = len(lis)
    for _ in range(length):
        for j in range(length-1):
            if sum(lis[j]) > sum(lis[j+1]):
                lis[j],lis[j+1] = lis[j+1],lis[j]
            elif sum(lis[j]) == sum(lis[j+1]) and lis[j+1][1] >lis[j][1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]

def main():
    '''Driver Code'''
    datasetnum = int(input())
    for _ in range(datasetnum):
        datanum = int(input())
        data = []
        for _ in range(datanum):
            data.append(list(map(int,input().split())))
        sort(data)
        printdata(data)
if __name__ == "__main__":
    main()
