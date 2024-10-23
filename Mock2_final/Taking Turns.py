'''Taking Turns'''
import json
import math
def taking_turn(arr:list) -> None:
    '''Rearrange list'''
    left = 0
    right = len(arr)-1
    new_arr = []
    for i in range(math.ceil(len(arr)/2)):
        if left >= right:
            new_arr.append(arr[left])
        elif not i%2:
            new_arr.append(arr[right])
            new_arr.append(arr[left])
            right -=1
            left +=1
        else:
            new_arr.append(arr[left])
            new_arr.append(arr[right])
            right -=1
            left +=1
    return new_arr
def main():
    '''Driver Code'''
    lis = json.loads(input())
    print(taking_turn(lis))
if __name__ == "__main__":
    main()
