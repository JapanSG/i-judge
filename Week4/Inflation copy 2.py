'''Inflation'''
def interest(cost,year):
    '''Calculate the compund interest'''
    for _ in range(year):
        cost = cost*10381//10000
    costS = str(cost)
    if cost <= 0:
        print("0.00")
    elif cost < 100:
        print("0."+costS[-2:])
    else:
        print(costS[:-2]+"."+costS[-2:])

def main():
    '''Driver Code'''
    interest(int(float(input())*100),int(input()))
main()
