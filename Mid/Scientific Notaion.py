'''Scientific Notation'''
##DON"T WORK
def trailing_zero(num : str):
    '''Return number of zero needed'''
    zero = 0
    for i in num:
        if i == "0":
            zero +=1
        elif i == ".":
            continue
        else:
            zero = 0
    if "." in num:
        return int(zero)
    else:
        return 0
def to_notation(num : float,zero : int)->str:
    '''Return scientific notation'''
    neg =""
    if num < 0:
        neg = "-"
        num = abs(num)
    power = 0
    if num == 0:
        return 0
    while num < 1:
        num *= 10
        power -= 1
    while num >= 10:
        num /= 10
        power += 1
    szero = "0"*zero
    if not power:
        return f"{neg}{num}{szero}"
    decimal = 0
    for _ in str(num):
        decimal += 1
    decimal = max(0,decimal-2)
    return f"{neg}{num:.{decimal}f}{szero} x 10^{power}"
def to_num(notation : str)->float:
    '''Return num'''
    a = ""
    string =""
    space_count = 0
    for i in notation:
        if i.isspace() and a =="":
            a = string
            string = ""
            space_count += 1
        elif i == "^":
            string = ""
        else:
            string += i
    power = string
    ans = float(a)*10**float(power)
    if ans == int(ans):
        return int(ans)
    return float(a)*10**float(power)
def main():
    '''Driver Code'''
    num = input()
    if "x" in num or "X" in num:
        print(f"{to_num(num)}")
    else:
        print(to_notation(float(num),trailing_zero(num)))
main()
