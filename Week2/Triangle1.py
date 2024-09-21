'''TriangleI'''
def main():
    '''driver code'''
    sides = [float(input()), float(input()), float(input())]
    most = 0
    if sides[0] > sides[1]:
        most = sides[0]
    else:
        most = sides[1]
    if sides[2] > most:
        most = sides[2]
    sides.remove(most)
    hypotenus = sides[0]**2 + sides[1]**2
    if hypotenus +0.01 >= most**2 >= hypotenus-0.01:
        print("Yes")
    else:
        print("No")
main()
