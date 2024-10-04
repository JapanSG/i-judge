'''isprime_small'''
def is_prime(val:int) -> bool:
    '''Check if val is a prime number'''
    if val in (0,1):
        return False
    i = 3
    prime = set([2])
    while i**2 <= val:
        if not val%i:
            return False
        for num in prime:
            if not i%num:
                i += 1
                continue
        prime.add(i)
        i += 2
    return True
def main():
    '''Driver Code'''
    if is_prime(int(input())):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()
