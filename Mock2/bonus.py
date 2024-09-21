'''bonus'''
def main():
    '''Driver Code'''
    salary = int(input())
    year = int(input())
    month = int(input())
    if month >= 10:
        year += 1
    if year >= 20:
        year = 20
    bonus = salary*year
    if bonus > 1000000:
        print(1000000)
    elif bonus < 5000:
        print(5000)
    else:
        print(bonus)
main()
