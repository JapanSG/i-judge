'''Ascending Sort'''
def main():
    '''Driver Code'''
    size = int(input())
    numlist = []
    for _ in range(size):
        num = int(input())
        numlist.append(num)
    numlist.sort()
    for i in numlist:
        print(i)
main()
