"""Train"""
STR1 = str(input())
STR1 += str(input())
NUM = int(input())
print(STR1)
STR2 = ""
for i in range(NUM):
    STR2 += STR1
    i += i
    i -= i
print(STR2)
