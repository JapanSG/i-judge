'''password'''
import math
def main():
    '''Driver Code'''
    password = input()
    length = len(password)
    pool = 0
    lower = False
    digit = False
    upper = False
    printable = False
    for i in password:
        if not digit and i.isdigit():
            pool += 10
            digit = True
        elif not lower and i.islower():
            pool += 26
            lower = True
        elif not upper and i.isupper():
            pool += 26
            upper = True
        elif not printable and i.isprintable() and not(i.isdigit() or i.islower() or i.isupper()):
            pool += 32
            printable = True
    entropy = math.floor(math.log2(pool**length))
    print(entropy)
    if entropy >= 128:
        print("Very Strong")
    elif entropy >= 60:
        print("Strong")
    elif entropy >= 36:
        print("Reasonable")
    elif entropy >= 28:
        print("Weak")
    else:
        print("Very Weak")
main()
