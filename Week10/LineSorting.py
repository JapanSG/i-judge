'''RAGH'''
def main():
    '''docstring'''
    amount = int(input())
    wordslist = []
    for _ in range(amount):
        line = input()
        inserted = False
        length = len(wordslist)
        for i in range(length):
            if len(line) < len(wordslist[i]):
                wordslist.insert(i,line)
                inserted = True
                break
        if not inserted:
            wordslist.append(line)
    for j in wordslist:
        print(j)
main()
