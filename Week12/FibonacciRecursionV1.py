'''FibonacciRecursionV1'''
def fib(num:int) -> int:
    '''Fib'''
    if num in (0,1):
        return num
    return fib(num-1)+fib(num-2)
def main():
    "Driver Code"
    print(fib(int(input())))
if __name__ == "__main__":
    main()
