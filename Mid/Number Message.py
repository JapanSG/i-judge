'''Number Message'''
def decode(code : str) -> str:
    '''return decoded message all capitalized'''
    code = code.replace("13","B")
    code = code.replace("12","R")
    code = code.replace("0","O")
    code = code.replace("5","S")
    code = code.replace("4","A")
    code = code.replace("3","E")
    code = code.replace("1","I")
    return code.upper()
def main():
    '''Driver Code'''
    code = input()
    message = decode(code)
    ans = ""
    for i in message:
        if i.isdigit():
            continue
        ans += i
    print(ans)
main()
