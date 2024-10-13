'''OneTwo'''
def onetwo(num:int) -> str:
    '''onetwo'''
    if num in (1,2):
        return str(num)
    return "".join((onetwo(num-1), onetwo(num-2)))
def main():
    '''Driver Code'''
    print(onetwo(int(input())))
if __name__ == "__main__":
    main()
