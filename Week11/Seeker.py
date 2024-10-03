'''Seeker'''
import re
def main():
    '''Driver Code'''
    pattern = "[0-9]+"
    message = input()
    print(sum(map(int, re.findall(pattern, message))))
if __name__ == "__main__":
    main()
