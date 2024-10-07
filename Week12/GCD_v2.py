'''GCD_v2'''
def gcd(num1:int, num2:int) -> int:
    '''Find greatest conmmon divisor'''
    if not num2:
        return num1
    return num1 if not num2 else gcd(num2,num1%num2)
if __name__ == "__main__":
    print(gcd(int(input()),int(input())))
