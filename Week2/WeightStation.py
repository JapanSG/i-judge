'''WeightStation'''
def main():
    '''driver code'''
    AVERAGE = float(input())
    FIRST = float(input())
    SECOND = float(input())
    THIRD = float(input())
    FORTH = (AVERAGE*4)-FIRST-SECOND-THIRD
    if AVERAGE*4 > 15000:
        print("Overweight")
    elif not AVERAGE+AVERAGE/2 > FIRST > AVERAGE-AVERAGE/2:
        print("Unbalance")
    elif not AVERAGE+AVERAGE/2 > SECOND > AVERAGE-AVERAGE/2:
        print("Unbalance")
    elif not AVERAGE+AVERAGE/2 > THIRD > AVERAGE-AVERAGE/2:
        print("Unbalance")
    elif not AVERAGE+AVERAGE/2 > FORTH > AVERAGE-AVERAGE/2:
        print("Unbalance")
    else:
        print(f"Pass {FORTH:.2f}")
main()
