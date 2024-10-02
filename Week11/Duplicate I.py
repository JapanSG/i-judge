'''Duplicate I'''
def main():
    '''Driver Code'''
    g1_num = int(input())
    g2_num = int(input())
    g1 = set()
    g2 = set()
    for _ in range(g1_num):
        g1.add(input())
    for _ in range(g2_num):
        g2.add(input())
    same = g1.intersection(g2)
    for student in sorted(same, key = int, reverse = True):
        print(student)
    if not same:
        print("Nope")
if __name__ == "__main__":
    main()
