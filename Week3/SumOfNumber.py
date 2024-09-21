"""SumOfNumber"""
def main():
    """SumOfNumber"""
    Sum = int(input())
    total = 0
    x = 0
    while x != -1 :
        total = total + x
        if total == Sum:
            break
        x = int(input())
    print(total)
main()
