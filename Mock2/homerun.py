'''homerun'''
def main():
    '''Driver Code'''
    n = int(input())
    capable = float(input())
    number_of_field = 0
    for _ in range(n):
        if float(input()) < capable:
            number_of_field += 1
    print(number_of_field)
main()
