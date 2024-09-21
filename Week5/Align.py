'''Align'''
def main():
    '''Driver Code'''
    size = int(input())
    align  = str(input())
    message = str(input())
    if align == "left":
        print(message)
    elif align == "center":
        print(" "*sum(divmod(size-len(message),2))+message)
    else:
        print(" "*(size-len(message))+message)
main()
