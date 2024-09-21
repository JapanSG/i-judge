'''Game'''
def main():
    '''Driver Code'''
    a_score = int(input())
    b_score = int(input())
    a_score_left = a_score%3
    b_score_left = b_score%3
    if a_score_left != b_score_left:
        print("Error")
    else:
        print(a_score_left)
main()
