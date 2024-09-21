'''Harshad'''
def main():
    '''Driver Code'''
    for _ in range(10):
        num = abs(int(input()))
        total = 0
        for i in str(num):
            total += int(i)
        if not total:
            print("No")
        elif num%total:
            print("No")
        else:
            print("Yes")
main()
