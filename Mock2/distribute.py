'''distribute'''
def main():
    '''Driver Code'''
    money = int(input())
    children = int(input())
    times = money//8
    money_used = times*8
    leftover = money%8
    i = 1
    if money_used > money or children-times > leftover:
        while money_used > money or children-times > leftover:
            money_used = (times-i)*8
            leftover = money-money_used
            i += 1
            if leftover > money:
                print(-1)
                return
        times -= i
    if leftover - (children-times) == 3 and children-times <= 1:
        times -= 1
    print(times)
main()
