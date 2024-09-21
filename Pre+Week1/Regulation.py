"""Regulation"""
a = int(input())
for i in range(30-len(str(a))):
    print(" ",end="")
print(a)
for i in range(30-len(str(a))):
    print(0,end="")
print(a)
b = float(input())
print("%.2f"%b)
print("%.12f"%b)
c = str(input())
for i in range(40-len(c)):
    print(" ",end="")
print(c)
