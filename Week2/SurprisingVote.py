'''SurprisingVote'''
def main():
    '''driver code'''
    total =  float(input())
    most = float(input())
    least = total-most*2
    if least < 0:
        least = 0
    if most - least > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
