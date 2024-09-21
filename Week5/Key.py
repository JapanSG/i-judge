'''Key'''
def main():
    '''Driver Code'''
    num = input()
    sumation = 0
    for i in num:
        sumation += int(i)
    product = int(num[-3:])*10
    if product+sumation <1000:
        print(f"{product+sumation+1000}"[-4:])
    else:
        print(f"{product+sumation}"[-4:])
main()
