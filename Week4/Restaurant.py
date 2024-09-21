'''Restaurant'''
def main():
    '''Driver Code'''
    cost = float(input())
    atleast = float(input())
    discount = float(input())
    additional = float(input())
    costadd = cost + additional
    if cost >= atleast:
        cost = cost*(1-discount/100)
    if costadd >= atleast:
        costadd = costadd*(1-discount/100)
    if cost > costadd:
        print("Yes",f"{cost-costadd:.3f}")
    elif cost < costadd:
        print("No",f"{costadd-cost:.3f}")
    else:
        print("Yes")
main()
