'''Diamond I'''
def my_zip(lis:list,iter_length:int):
    '''zip all list in list'''
    zip_list =[]
    for i in range(iter_length):
        mini = []
        for j in lis:
            mini.append(j[i])
        zip_list.append(mini)
    return zip_list

def main():
    '''Driver Code'''
    depth = int(input())
    width = int(input())
    land = []
    for _ in range(depth):
        land.append(list(map(int,input().split())))
    print(max(list(map(sum, my_zip(land,width)))))
if __name__ == "__main__":
    main()
