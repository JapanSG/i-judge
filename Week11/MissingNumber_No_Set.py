'''MissingNumber_No_Set'''
def find_missing_num(max_num) -> list:
    '''Find missing num'''
    numbers = list(range(1,max_num+1))
    while True:
        num = int(input())
        if not num:
            return numbers
        if num in numbers:
            numbers.remove(num)
def main():
    '''Driver Code'''
    max_num = int(input())
    missing_numbers = find_missing_num(max_num)
    for num in missing_numbers:
        print(num)
if __name__ == "__main__":
    main()
