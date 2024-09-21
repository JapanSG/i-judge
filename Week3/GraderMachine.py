'''GraderMachine'''
def main():
    '''driver code'''
    x = int(input())
    y = int(input())
    order = 1
    z = 1
    if x > y:
        order = -1
        z = -1
    total = 0
    print("pass :", end = "")
    for i in range(x,y+z,order):
        if not i%2:
            total += i
            print("",i,end = "")
    print("")
    print("Sum :", total)
main()
