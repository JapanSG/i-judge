'''chacha'''
import math
def main() -> None:
    '''Driver Code'''
    total_day = int(input())
    salary = 0
    for _ in range(total_day):
        hours = math.ceil(float(input()))
        salary += hours*8720
    print(salary)
main()
