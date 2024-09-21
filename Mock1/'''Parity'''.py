'''Parity'''
def main():
    '''Driver Code'''
    bits = input()
    pari  =input()
    total = 0
    for i in bits:
        if int(i):
            total += 1
    if pari == "Even" and total%2:
        print(bits+"1")
    elif pari == "Odd" and not total%2:
        print(bits+"1")
    else:
        print(bits+"0")
main()
