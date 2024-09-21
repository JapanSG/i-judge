'''DimondII'''
def best(arr:list,level:int,index:int,max_level,max_index : int):
    '''Find the most and best total'''
    if level == max_level:
        if index <= 0:
            return max(arr[level][index+1],arr[level][index])
        if index >= max_index-1:
            return max(arr[level][index],arr[level][index-1])
        return max(arr[level][index+1],arr[level][index],arr[level][index-1])
    if index == 0:
        return max(best(arr,level+1,index,max_level,max_index),best(arr,level+1,index+1,max_level,max_index))+arr[level][index]
    if index == max_index:
        return max(best(arr,level+1,index,max_level,max_index),best(arr,level+1,index-1,max_level,max_index))+arr[level][index]
    return max(best(arr,level+1,index,max_level,max_index),best(arr,level+1,index-1,max_level,max_index),best(arr,level+1,index+1,max_level,max_index))+arr[level][index]
def main():
    '''Driver Code'''
    num_arr = int(input())
    num_element = int(input())
    arr = []
    ans = []
    for _ in range(num_arr):
        arr.append(list(map(int,input().split())))
    for i in range(num_element):
        ans.append(best(arr,0,i,num_arr-1,num_element-1))
    print(max(ans))
