'''Ink'''
import math
def main():
    '''Driver Code'''
    data = input().split()
    rate = int(data[0])
    people = int(data[1])
    for _ in range(people):
        cords = [int(point) for point in input().split()]
        time = (cords[0]**2 + cords[1]**2)*3.1416/rate
        print(math.ceil(time))
if __name__ == "__main__":
    main()
