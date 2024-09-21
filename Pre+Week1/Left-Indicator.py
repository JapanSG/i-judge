"""left"""
width = int(input())
height = int(input())
space = int(height/2)
c = space
while c > 0 :
    LINE = ""
    for j in range(c):
        j += 1
        j -= 1
        LINE = LINE + " "
    for j in range(width):
        j += 1
        j -= 1
        LINE = LINE +"*"
    print(LINE)
    c = c-1
if height%2:
    LINE = ""
    for k in range(width) :
        k += 1
        k -= 1
        LINE  = LINE + "*"
    print(LINE)
for i in range(space) :
    LINE = " "
    for j in range(i) :
        j += 1
        j -= 1
        LINE = LINE + " "
    for j in range(width) :
        j += 1
        j -= 1
        LINE = LINE + "*"
    print(LINE)
