'''Flatten'''
import json
def flatten(lis:list)->list:
    '''flatten'''
    new = []
    for i in lis:
        if isinstance(i,list):
            new.extend(flatten(i))
        else:
            new.append(i)
    return new
def main():
    '''Driver Code'''
    lis = json.loads(input())
    print(sorted(flatten(lis), reverse = True))
if __name__ == "__main__":
    main()
