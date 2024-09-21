'''PostOffice'''
def get_envelop_cost(weight : float)-> int:
    '''Return cost based on weight'''
    if weight > 1000:
        return 68
    if weight > 500:
        return 48
    if weight > 250:
        return 33
    if weight > 100:
        return 28
    if weight > 20:
        return 23
    if weight > 10:
        return 18
    return 16
def get_package_cost(weight : float)-> int:
    '''Return cost based on weight'''
    if weight > 1000:
        return 70
    if weight > 500:
        return 55
    return 45
def main():
    '''Driver Code'''
    envelop = int(input())
    package = int(input())
    total_cost = 0
    for _ in range(envelop):
        weight = float(input())
        total_cost += get_envelop_cost(weight)+13
    for _ in range(package):
        weight = float(input())
        total_cost += get_package_cost(weight)+15
    print(total_cost)
main()
