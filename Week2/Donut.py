'''Donut'''
def main():
    '''driver code'''
    cost = int(input())
    donut = int(input())
    free = int(input())
    need = int(input())
    dset = donut + free
    numberOfSet = need//dset
    donutNeeded = need-numberOfSet*dset
    totalDonut1 = numberOfSet*dset+(donutNeeded)
    totalCost1 = numberOfSet*donut*cost+donutNeeded*cost
    totalDonut2 = (numberOfSet+1)*dset
    totalCost2 = (numberOfSet+1)*donut*cost
    if totalCost1 < totalCost2:
        print(totalCost1,totalDonut1)
    else:
        print(totalCost2,totalDonut2)
main()
