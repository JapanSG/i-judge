'''Stuttering'''
def main():
    '''Driver Code'''
    message = input()
    lis = message.split()
    i = 1
    while i < len(lis):
        while i < len(lis) and lis[i] == lis[i-1]:
            lis.pop(i)
        i += 1
    print(*lis)
main()
