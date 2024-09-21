'''ValidVar'''
def isvalidvar(string):
    "Check if string is a valid variable name"
    temp1 = ["if","else","elif","while","for","True","False","continue","break","return","is"]
    restrict = ["in","and","or","from","as","pass","not","def","None"] + temp1
    for i in restrict:
        if i == string:
            return False
    if string[0].isdigit():
        return False
    for i in string:
        if not i.isdigit() and not i.isalpha() and not i == "_":
            return False
    return True
def main():
    '''Driver Code'''
    for _ in range(int(input())):
        x = input().strip()
        if isvalidvar(x):
            print("Valid")
        else:
            print("Invalid")
main()
