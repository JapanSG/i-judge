'''bad_keyboard'''
def swap(a,b,message):
    '''replace 2 letter'''
    message = message.replace(a,"asdasdasd")
    message = message.replace(b,a)
    message = message.replace("asdasdasd",b)
    return message
def main():
    '''Driver Code'''
    message = input()
    message = swap("i","o",message)
    message = swap("I","O",message)
    print(message)
main()
