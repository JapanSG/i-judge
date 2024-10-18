'''Calculator V2'''
def main():
    '''Driver Code'''
    num = input()
    if num == "1":
        print(1)
        return
    num = num[::-1]
    length = len(num)
    total = 0
    for i in range(1,length):
        total += (i+1)*(9*10**(i-1))
    sumed = '9'*(length-1)
    if not sumed:
        sumed = 0
    else:
        sumed = int(sumed)
    total += (int(num[::-1]) - int(sumed))*(length+1)
    print(total)
if __name__ == "__main__":
    main()
