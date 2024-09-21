'''Coke'''
def main():
    '''Driver Code'''
    original_price = int(input())
    cap = int(input())
    discounted_price = int(input())
    needed = int(input())
    bought = 0
    cost = 0
    unused_cap = 0
    if not cap:
        discounted_price = original_price
    while bought < needed:
        if unused_cap >= cap:
            cost += discounted_price
            unused_cap -= cap
        else:
            cost += original_price
        bought += 1
        unused_cap += 1
    print(cost)
main()
