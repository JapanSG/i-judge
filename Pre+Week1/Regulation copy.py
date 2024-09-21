"""Regulation"""
a = int(input())
b = float(input())
c = str(input())
w = ""
w1 = ""
for i in range(30 - len(str(a))):
    w += " "
z = w.replace(" ","0")
# if len(str(a)) > 30:
#     print(str(a)[:30])
#     print(str(a)[:30])
# else:
#     print(w+str(a))
#     print(z+str(a))
print(w+str(a))
print(z+str(a))

print(f"{b:0,.2f}")
print(f"{b:0,.12f}")

for i in range(40-len(str(c))):
    w1 += " "
if len(c) > 40:
    print(c[:40])
else:
    print(w1+c)
