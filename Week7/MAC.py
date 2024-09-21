'''MAC'''
def which_method(address:str)->int:
    '''Return which MAC address method is used'''
    if "-" in address:
        return 1
    if ":" in address:
        return 2
    if "." in address:
        return 3
    return -1
def check(address:str,end_pos:int,end_char:str)->bool:
    '''Return True if Mac Address is valid else return False'''
    count = 0
    for i in address:
        if count%(end_pos+1) == end_pos and i != end_char:
            return False
        if count%(end_pos+1) != end_pos and not i.isdigit() and not i.upper() in "ABCDEF":
            return False
        count += 1
    return True
def main():
    '''Driver Code'''
    address = input()
    method = which_method(address)
    if method == 1 and (not check(address,2,"-") or len(address) !=17):
        print("ERROR")
        return
    if method == 2 and (not check(address,2,":") or len(address) !=17):
        print("ERROR")
        return
    if method ==3 and (not check(address,4,"." or len(address) !=14)):
        print("ERROR")
        return
    if method == -1:
        print("ERROR")
        return
    print(f"VALID {method}")
if __name__ == "__main__":
    main()
