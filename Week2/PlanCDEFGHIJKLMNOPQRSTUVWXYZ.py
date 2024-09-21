'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''    
def main():
    '''driver code'''
    COMMAND = str(input())
    FIRST = float(input())
    SECOND = float(input())
    THIRD = float(input())
    most = 0
    least = 0
    mid = 0
    if FIRST >= SECOND:
        most = FIRST
        mid = SECOND
    else:
        most = SECOND
        mid = FIRST
    if THIRD <= mid:
        least = THIRD
    else:
        least = mid
        if THIRD > most:
            mid = most
            most = THIRD
        else:
            mid = THIRD
    if COMMAND == "Ascend":
        print(f"{least:.2f}, {mid:.2f}, {most:.2f}")
    else:
        print(f"{most:.2f}, {mid:.2f}, {least:.2f}")
main()
