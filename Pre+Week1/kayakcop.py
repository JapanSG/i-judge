"""Kayak"""
n = int(input())
lis = sorted(list(map(int,input().split())))
totals = []

for i in range(2*n):
    for j in range(i):
        temp = 0
        c = 0
        k = 0
        l = -1
        while c < n-1:
            k = l + 1
            while k == i or k== j:
                k += 1
            l = k + 1
            while l == i or l == j:
                l += 1
            temp += lis[l]-lis[k]
            c += 1
        totals.append(temp)
print(min(totals))
print(totals)
