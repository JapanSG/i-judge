"""largest number"""
def recursion(num1,num2,num3,counter=0):
    '''
    This function returns the largest possible number made out of three different integers.
    param1 : integer as string
    param2 : integer as string
    param3 : integer as string
    param4 : recursive counter
    '''
    if counter >= 3:
        return "0"
    first =""
    if int(num1+num2+num3) > int(num1+num3+num2):
        first = num1+num2+num3
    else:
        first = num1+num3+num2
    second = recursion(num3,num1,num2,counter = counter+1)
    if int(first) > int(second):
        return first
    return second

def main():
    """Driver Code"""
    NUM1 = str(input())
    NUM2 = str(input())
    NUM3 = str(input())
    print(recursion(NUM1,NUM2,NUM3))
main()
