'''CoffeeShop'''
def coffee(price : float, discount1 : float, discount2 : float, discount2_require : float, cups):
    '''Get Price'''
    first_price = price + price*(1-discount1/100)*(cups-1)
    second_price = price*cups
    if second_price >= discount2_require:
        second_price *= 1-discount2/100
    if first_price < second_price:
        print(1)
        print(f"{first_price:.2f}")
    else:
        print(2)
        print(f"{second_price:.2f}")

def main():
    '''Driver Code'''
    price = float(input())
    discount1 = float(input())
    discount2 = float(input())
    discount2_require = float(input())
    cups = int(input())
    coffee(price,discount1,discount2,discount2_require,cups)
main()
