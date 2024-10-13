'''CoPrimeV1'''
def gcd(val1:int,val2:int) -> int:
    '''find greatest common denominator'''
    if not val2:
        return val1
    return gcd(val2,val1%val2)
def main():
    '''Driver Code'''
    gcd_num = gcd(int(input()),int(input()))
    if gcd_num == 1:
        print("YES")
    else:
        print("NO")
    print(gcd_num)
if __name__ == "__main__":
    main()
