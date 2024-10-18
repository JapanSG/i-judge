'''Coke V2'''
def coke(price:int, cap:int, dis:int, num:int) -> int:
    '''coke'''
    if not cap:
        dis = price
        cap = num
    dis_num,r = divmod(num,cap)
    if not r and not dis_num:
        return price*num
    if not r:
        dis_num -= 1
    return dis_num*dis+(num-dis_num)*price
def main():
    '''Driver Code'''
    price = int(input())
    cap = int(input())
    dis = int(input())
    num = int(input())
    print(coke(price,cap,dis,num))
if __name__ == "__main__":
    main()
