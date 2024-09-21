'''Inflation'''
import decimal
from decimal import Decimal
from decimal import getcontext
def main():
    '''Driver Code'''
    getcontext().prec = 4
    cost = float(input())
    year = int(input())
    final = cost*(1.0381)**year
    getcontext().rounding = decimal.ROUND_FLOOR
    ans = Decimal(final)
    print(ans)
main()
