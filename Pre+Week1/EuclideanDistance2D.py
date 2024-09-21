"""EuclideanDistance2D"""
import math
lis = [0,0,0,0]
for i in range(4):
    lis[i] = float(input())
print(math.sqrt(((lis[0]-lis[2])**2)+((lis[1]-lis[3])**2)))
