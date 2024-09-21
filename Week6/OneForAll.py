'''One For All'''
def main():
    '''Driver Code'''
    num = int(input())
    message = ""
    for i in range(num-1):
        if not i%2:
            message += input()+"*"*(i+1)
        else:
            message += input()+"-"*(i+1)
    if num:
        message += input()+f"_{num}"
    print(message)
main()
