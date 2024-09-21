"""FoodGrade1"""
def check(count=0,num = 0):
    '''Check input'''
    if num >= 24:
        return count
    if 50 <= int(input()) <= 70:
        return check(count+1,num+1)
    return check(count,num+1)
def main():
    '''Driver Code'''
    print(check())
main()
