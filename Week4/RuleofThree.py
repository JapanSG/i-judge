'''RuleofThree'''
def main():
    '''Driver Code'''
    num = int(input())
    least = 0
    min_weight = 0
    min_price = 0
    for _ in range(num):
        price = float(input())
        weight = float(input())
        if least < weight/price:
            least = weight/price
            min_weight = weight
            min_price = price
        elif least == weight/price and price < min_price:
            least = weight/price
            min_weight = weight
            min_price = price
    print(f'{min_price:.2f} {min_weight:.2f}')
main()
