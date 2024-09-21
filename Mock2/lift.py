'''lift'''
def main():
    '''Driver Code'''
    n_people = int(input())
    limit_weight = float(input())
    total_weight = 0
    there_is_kids = False
    there_is_adults = False
    for _ in range(n_people):
        age = int(input())
        if age >= 12:
            there_is_adults = True
        else:
            there_is_kids = True
        weight = float(input())
        total_weight += weight
    if total_weight > limit_weight:
        print("Not Safe")
    elif there_is_kids and not there_is_adults:
        print("Not Safe")
    else:
        print("Safe")
main()
