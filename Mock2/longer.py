'''longer'''
import math
def main():
    '''Driver Code'''
    circle_radius = float(input())
    rectangle_width = float(input())
    rectangle_height = float(input())
    circumfurence = 2*math.pi*circle_radius
    side = (rectangle_height+rectangle_width)*2
    if circumfurence > side:
        print("Circle is longer")
    elif circumfurence < side:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f'{abs(circumfurence-side):.5f}')
main()
