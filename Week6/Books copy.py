'''Books'''
import math
def main():
    '''Driver Code'''
    book = int(input())
    page = int(input())
    x = int(input())
    y = int(input())
    day = 0
    for i in range(book):
        pageleft = page
        if math.ceil(page*(x/y)) >= pageleft:
            day +=  book-i
            break
        while pageleft > 0:
            pageleft -= math.ceil(page*(x/y))
            x,y,day = x+1,y+1,day+1
    print(day)
main()
