'''Inflation'''
import decimal
from decimal import Decimal
from decimal import getcontext
def main():
    '''Driver Code'''
    cost = Decimal(input())
    year = int(input())
    getcontext().prec = len(str(cost)) + 2
    getcontext().rounding = decimal.ROUND_DOWN 
    # print(cost*(Decimal(1+3.81/100))**year)
    for _ in range(year):
        cost = cost*Decimal(1.0381)
    print(cost)
main()
