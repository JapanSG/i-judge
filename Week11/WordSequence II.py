'''WordSequence II'''
def main():
    '''Driver Code'''
    base = input()
    change = input()
    length = max(len(base),len(change))
    base = f"{base:{length}s}"
    change = f"{change:{length}s}"
    for i in range(-1,length):
        print(f"{change[:i+1].strip()}{base[i+1:]}".strip())
if __name__ == "__main__":
    main()
