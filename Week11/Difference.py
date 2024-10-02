'''Difference'''
def main():
    '''Driver Code'''
    set_a = set()
    set_b = set()
    a_num = int(input())
    b_num = int(input())
    for _ in range(a_num):
        set_a.add(int(input()))
    for _ in range(b_num):
        set_b.add(int(input()))
    set_a = set(set_a)
    set_b = set(set_b)
    set_a.difference_update(set_b)
    for member in sorted(set_a):
        print(member,end=" ")
if __name__ == "__main__":
    main()
