'''BigFrame'''
def main():
    '''Driver Code'''
    lis = [0,0,0,0,0]
    length = 0
    for i in range(5):
        lis[i] = input().strip()
        length = max(len(lis[i]),length)
    print("*"*(length+4))
    for i in lis:
        print(f"* {i:<{length}s} *")
    print("*"*(length+4))
main()
