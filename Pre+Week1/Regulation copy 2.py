"""Regulation"""
a = int(input())
b = float(input())
C = str(input())
#print("%30d"%a)
#print("%030d"%a)
#print("%40s"%C)
print(f"{a:30d}")
print(f"{a:030d}")
#print("%.2f"%b)
#print("%.12f"%b)
print(f"{b:.2f}")
print(f"{b:.12f}")
print(f"{C:>40s}")
