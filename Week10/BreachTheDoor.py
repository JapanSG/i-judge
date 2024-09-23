'''BreachTheDoor'''
import re
def print_single_ln(lis:list):
    '''Print list into a single line'''
    for obj in lis:
        print(obj,end = " ")
def remove_word(lis:list,size:int):
    '''Remove all string in lis that have less than length'''
    i = 0
    while i < len(lis):
        if len(lis[i]) <= size:
            lis.pop(i)
        else:
            i+=1
def main():
    '''Driver Code'''
    message = re.sub(r"[\W0-9]"," ",input())
    message = message.split()
    remove_word(message,6)
    print_single_ln(message)
if __name__ == "__main__":
    main()
