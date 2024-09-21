'''Lotto'''
def main():
    '''Driver Code'''
    first = int(input())
    last_two = input()
    first_three1 = input()
    first_three2 = input()
    last_three1 = input()
    last_three2 = input()
    lotto = input()
    second = first+1
    third = first-1
    if first == 999999:
        second = 0
    if not first:
        third = 999999
    winnings = 0
    if f"{lotto:>06s}" == f"{first:>06d}":
        winnings += 6000000
    elif f"{lotto:>06s}" == f"{second:>06d}" or f"{lotto:>06s}" == f"{third:>06d}":
        winnings += 100000
    if f"{lotto:>06s}"[-2:] == f"{last_two:>02s}":
        winnings += 2000
    if f"{lotto:>06s}"[:3] == f"{first_three1:>03s}":
        winnings += 4000
    if f"{lotto:>06s}"[:3] == f"{first_three2:>03s}":
        winnings += 4000
    if f"{lotto:>06s}"[-3:] == f"{last_three1:>03s}":
        winnings += 4000
    if f"{lotto:>06s}"[-3:] == f"{last_three2:03s}":
        winnings += 4000
    print(winnings)
main()
