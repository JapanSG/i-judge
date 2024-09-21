'''B - Fully pair?'''
# def list_str(lis:list)->str:
#     '''Return str of all element in list'''
#     string = ""
#     for i in lis:
#         string += i
#     return string
def main():
    '''Driver Code'''
    string = input()
    no_pair = ""
    for i in string:
        if string.count(i)%2:
            no_pair += i
        string = string.replace(i,"")
    #no_pair = list_str(sorted(no_pair))
    if not no_pair:
        print("fully paired")
    else:
        print(no_pair)
if __name__ == "__main__":
    main()
