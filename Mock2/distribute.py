'''distribute'''
def eight(money:int,children:int) -> int:
    '''find how many child get 8'''
    if children > money or (money == 4 and children == 1):
        return -1
    if money < 8:
        return 0
    times = money//8
    left = money%8
    if times > children or (times == children and left > 0):
        return children-1
    if left == 4 and children-times == 1:
        return times-1
    if left < children - times: ## 25 testcase issue here children aprox(8.795*10**23)
        temp = ((children-times)-left)//7
        if ((children-times)-left)%7:
            temp += 1
        times -= temp
    return int(times)
def main():
    '''Driver Code'''
    money = int(input())
    children = int(input())
    print(eight(money,children))
# for i in range(1,107):
#     print(f"money = {106} children = {i} ans = {eight(106,i)}")
main()
