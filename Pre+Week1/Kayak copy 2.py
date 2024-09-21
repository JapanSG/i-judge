"""kayak"""
def leastdif(arr):
    "return the difference of the pair that has the least difference and remove them from the list"
    least = 1000000
    left = 0
    for i in range(len(arr)-1):
        dif = arr[i+1] - arr[i]
        if dif < least:
            least = dif
            left = i
    arr.pop(left+1)
    arr.pop(left)
    return least

n = int(input())
lis = sorted(list(map(int,input().split())))
ANS = 0
for k in range(n-1):
    k += 0
    ANS += leastdif(lis)
print(ANS)
