'''isprime_small'''
def is_prime(val:int) -> bool:
    '''Check if val is a prime number'''
    if val in (0,1):
        return False
    i = 2
    prime = set()
    while i**2 <= val:
        if not val%i:
            return False
        for num in prime:
            if not i%num:
                i += 1
                continue
        prime.add(i)
        i += 1
    return True
def main():
    '''Driver Code'''
    if is_prime(int(input())):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
