'''Debaratna Road'''
def main():
    '''Driver Code'''
    dis = float(input())
    if 0 <= dis <= 5.032:
        print("Bangkok")
    elif 5.032 < dis <= 35.477:
        print("Samut Prakarn")
    elif 35.477 < dis <= 52.900:
        print("Chachoengsao")
    elif 52.900 < dis <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
main()