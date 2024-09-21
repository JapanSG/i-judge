'''Century'''
import math
def get_year_ad(string:str)->int:
    '''Return the year in A.D.'''
    if "B.E." in string:
        return int(string[5:])-543
    return int(string[5:])
def main():
    '''Driver Code'''
    num = int(input())
    for _ in range(num):
        year = get_year_ad(input())
        if year < 0 :
            print("ERROR")
        else:
            print(math.ceil(year/100))
if __name__ == "__main__":
    main()
