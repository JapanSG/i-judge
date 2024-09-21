'''FOR!F-Ball'''
def main():
    '''Driver Code'''
    moves = input()
    left = True
    mid = False
    right = False
    for i in moves:
        if i == "A":
            left, mid = mid, left
        elif i == "B":
            mid, right = right, mid
        else:
            left, right = right, left
    if left:
        print(1)
    if mid:
        print(2)
    if right:
        print(3)
main()
