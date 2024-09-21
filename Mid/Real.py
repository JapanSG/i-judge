'''Real'''
def is_on(string : str):
    '''Return True if string == "on" else return False'''
    if string == "on":
        return True
    return False
def get_val(a,b,c,d,e,f,g,dp)->str:
    '''Get val'''
    ans = ""
    lis = [0,0,0,0,0,0,0,0,0,0]
    lis[0]= a and b and c and d and e and f and not g
    lis[1] = not a and b and c and not d and not e and not f and not g
    lis[2] = a and b and not c and d and e and not f and g
    lis[3] = a and b and c and d and not e and not f and g
    lis[4] = not a and b and c and not d and not e and f and g
    lis[5] = a and not b and c and d and not e and f and g
    lis[6] = a and not b and c and d and e and f and g
    lis[7] = a and b and c and not d and not e and not f and not g
    lis[8] = a and b and c and d and e and f and g
    lis[9] = a and b and c and d and not e and f and g
    if lis[0]:
        ans += "0"
    elif lis[1]:
        ans += "1"
    elif lis[2]:
        ans += "2"
    elif lis[3]:
        ans += "3"
    elif lis[4]:
        ans += "4"
    elif lis[5]:
        ans += "5"
    elif lis[6]:
        ans += "6"
    elif lis[7]:
        ans += "7"
    elif lis[8]:
        ans += "8"
    elif lis[9]:
        ans += "9"
    else:
        return "_"
    if dp:
        ans +="."
    return ans
def main():
    '''Driver Code'''
    num = ""
    for _ in range(3):
        num += get_val(is_on(input()),is_on(input()),is_on(input()),is_on(input()),
                       is_on(input()),is_on(input()),is_on(input()),is_on(input()))
    if "_" in num or num.count(".") > 1:
        print("Error")
    else:
        print(f"{float(num):.2f}")
main()
