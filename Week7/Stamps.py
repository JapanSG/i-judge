'''Stamps'''
import math
def main() -> None:
    '''Drive Code'''
    times = int(input())
    stamps_requirement = int(input())#a
    stamps_received = int(input())#b
    discount_requirment = int(input())#c
    discount = int(input())#d
    stamps = 0
    total_cost = 0
    for _ in range(times):
        cost = int(input())
        if not discount:
            discount_used = 0
        else:
            discount_used = math.ceil(min(stamps//discount_requirment,cost/discount))
        cost = max(cost-discount_used*discount,0)
        stamps -= discount_used*discount_requirment
        total_cost += cost
        stamps += (cost//stamps_requirement)*stamps_received
    print(total_cost)
    print(stamps)
if __name__ == "__main__":
    main()
