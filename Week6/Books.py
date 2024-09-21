'''Books'''
import math
def main():
    '''Driver Code'''
    book = int(input())
    page = int(input())
    x = int(input())
    y = int(input())
    day = 0
    acu = 0
    pageleft = page*book
    while pageleft > 0:
        read = math.ceil(page*(x/y))
        if acu >= page:
            pageleft += acu-page
            acu = 0
        pageleft -= read
        acu += read
        x += 1
        y += 1
        day += 1
    print(day)
main()
