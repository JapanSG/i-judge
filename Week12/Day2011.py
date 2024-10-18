'''Day2011'''
def main():
    '''Driver Code'''
    days = {
        1 : "Saturday",
        2 : "Sunday",
        3 : "Monday",
        4 : "Tuesday",
        5 : "Wednesday",
        6 : "Thursday",
        0 : "Friday"
    }
    months = {
        1 : 0,
        2 : 31,
        3 : 31+28,
        4 : 31+28+31,
        5 : 31+28+31+30,
        6 : 31+28+31+30+31,
        7 : 31+28+31+30+31+30,
        8 : 31+28+31+30+31+30+31,
        9 : 31+28+31+30+31+30+31+31,
        10: 31+28+31+30+31+30+31+31+30,
        11: 31+28+31+30+31+30+31+31+30+31,
        12: 31+28+31+30+31+30+31+31+30+31+30
    }
    day = int(input())
    month = int(input())
    print(days[(months[month]+day)%7])
if __name__ == "__main__":
    main()
