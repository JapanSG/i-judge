"""HamBURGER"""
bread1 = int(input())
bread2 = int(input())
BURGER = ""
for i in range(bread1):
    i += 1
    i -= 1
    BURGER = BURGER + "|"
for i in range((bread1+bread2)*2):
    i += 1
    i -= 1
    BURGER = BURGER + "*"
for i in range(bread2):
    i += 1
    i -= 1
    BURGER = BURGER + "|"
print(BURGER)
