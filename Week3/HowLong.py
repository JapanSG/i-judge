"""HowLong"""
def main():
    """HowLong"""
    x = int(input())
    s = str(x)
    y = 0
    for _ in s:
        y = y+1
    if x < 0:
        print(y-1)
    else:
        print(y)
main()
