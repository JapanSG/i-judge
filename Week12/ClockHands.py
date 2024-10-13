'''ClockHands'''
def main():
    '''Driver Code'''
    hour = int(input())
    minute = int(input())
    hour_hand_pos = hour*5+minute/12
    if hour_hand_pos >= minute and hour_hand_pos - minute < 1:
        print(True)
    else:
        print(False)
if __name__ == "__main__":
    main()
