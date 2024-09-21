'''Parallelogram'''
def main():
    '''Driver Code'''
    message = input()
    length = len(message)
    for i in range(length):
        print(" "*(length-i-1),message[0:i+1],sep = "")
    for i  in range(length-1):
        print(message[i+1:])
main()
