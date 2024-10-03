'''MissingNumber'''
def find_missing_num_set(max_num) -> set:
    '''Find missing num using set'''
    universe = set(range(1,max_num + 1))
    set_a = set()
    while True:
        num = int(input())
        if not num:
            return universe.difference(set_a)
        set_a.add(num)
def main():
    '''Driver Code'''
    missing_numbers = find_missing_num_set(int(input()))
    for num in sorted(missing_numbers):
        print(num)
if __name__ == "__main__":
    main()
