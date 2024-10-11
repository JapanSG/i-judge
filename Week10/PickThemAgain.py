'''PickThem'''
def main():
    ''':d'''
    nums = input()
    final = list(map(int,nums.split()))
    even = False
    for i in reversed(final):
        if not i % 3 or not i % 5:
            even = True
            print(i)
    if not even:
        print("Nope")
main()
