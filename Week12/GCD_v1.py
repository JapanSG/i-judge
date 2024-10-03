'''GCD_v1'''
def gcd(*vals:int)->int:
    '''Return greatest common denominator'''
    vals = [val for val in vals if val]
    least = min(vals)
    for num in range(least,0,-1):
        is_gcd = True
        for val in vals:
            if val%num:
                is_gcd = False
                continue
        if is_gcd:
            return num
    raise ValueError
def main():
    '''Driver Code'''
    print(gcd(int(input()),int(input())))
if __name__ == "__main__":
    main()
