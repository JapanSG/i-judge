'''Netflix'''
import math
def yes_no(string):
    '''Return bool'''
    return bool(string == "Yes")
def main():
    '''Driver Code'''
    num_screen = int(input())
    num_download = int(input())
    input()
    input()
    tv = yes_no(input())
    hd = yes_no(input())
    ultra = yes_no(input())
    if ultra:
        premium_num = max(math.ceil(num_screen/4),math.ceil(num_download/4))
        print(f"Premium x {premium_num}")
        print(f"Total = {premium_num*419} THB")
    elif hd:
        if max(num_screen,num_download)%4 in (0,3):
            premium_num = max(math.ceil(num_screen/4),math.ceil(num_download/4))
            print(f"Premium x {premium_num}")
            print(f"Total = {premium_num*419} THB")
        elif (num_screen%4 in (1,2) or num_download%4 in (1,2)):
            premium_num = max(num_screen//4,num_download//4)
            if max(num_screen,num_download) > 3:
                print(f"Premium x {premium_num}")
            print(f"Standard x {1}")
            print(f"Total = {premium_num*419+349} THB")
    elif tv:
        if max(num_screen,num_download)%4 in (0,3):
            premium_num = max(math.ceil(num_screen/4),math.ceil(num_download/4))
            print(f"Premium x {premium_num}")
            print(f"Total = {premium_num*419} THB")
        elif num_screen%4 == 2 or num_download%4 == 2:
            premium_num = max(num_screen//4,num_download//4)
            if max(num_screen,num_download) > 3:
                print(f"Premium x {premium_num}")
            print(f"Standard x {1}")
            print(f"Total = {premium_num*419+349} THB")
        else:
            premium_num = max(num_screen//4,num_download//4)
            if max(num_screen,num_download) > 3:
                print(f"Premium x {premium_num}")
            print(f"Basic x {1}")
            print(f"Total = {premium_num*419+279} THB")
    else:
        mobile_num = max(num_screen,num_download)
        print(f"Mobile x {mobile_num}")
        print(f"Total = {mobile_num*99} THB")
main()
