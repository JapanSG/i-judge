'''Facebook'''
def main():
    '''Driver Code'''
    friends = {}
    f1,f2 = "",""
    while True:
        data = input()
        if "?" in data:
            f1,f2 = data.split(" ? ")
            break
        t1,t2 = data.split(" <-> ")
        friends[t1] = friends.get(t1,set()).union(set([t2]))
        friends[t2] = friends.get(t2,set()).union(set([t1]))
    if f1 not in friends or f2 not in friends:
        print("No mutual friend")
        return
    mutual_friends = friends[f1].intersection(friends[f2])
    if not mutual_friends:
        print("No mutual friend")
    else:
        for i in sorted(mutual_friends):
            print(i)
if __name__ == "__main__":
    main()
