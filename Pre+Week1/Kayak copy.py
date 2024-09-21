n = int(input())
lis = sorted(list(map(int,input().split())))
print(lis)
totals =[]
for i in range((2*n)-1) :
    for j in range(i+1,2*n) :
        newlis = lis[:i] + lis[i+1:j] + lis[j+1:]
        temp = sum(newlis[1::2]) - sum(newlis[::2])
        totals.append(temp)
print(min(totals))
