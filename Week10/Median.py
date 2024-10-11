'''Median'''
def med():
    '''mid'''
    amount = int(input())
    medlist = []
    for _ in range(amount):
        medlist.append(float(input()))
    medlist.sort()
    middle = (amount + 1) // 2
    if not amount % 2:
        print(f"{(medlist[middle-1]+medlist[middle])/2:.3f}")
    else:
        print(f"{medlist[middle-1]:.3f}")
med()
