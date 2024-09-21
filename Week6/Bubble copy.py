'''bubble'''
def recursive(track : str, times : int, i : int):
    length = len(track)
    '''
    Check which path is the fastest when faced with a "O" bubble recursively and return times, True
    If not possible return Shortest path to the finished line, False
    '''
    if track[i+3] == " ":
        temp3,is_possible3 = length-i-1, False
    else:
        temp3,is_possible3 = race(track,times+1,i+3)
    if track[i+2] == " ":
        temp2,is_possible2 = length-i-1, False
    else:
        temp2,is_possible2 = race(track,times+1,i+2)
    if track[i+1] == " ":
        temp1,is_possible1 = length-i-1, False
    else:
        temp1,is_possible1 = race(track,times+1,i+1)
    possible = [is_possible3,is_possible2,is_possible1]
    num = [temp3,temp2,temp1]
    least = 10000
    impossible = True
    for j in range(3):
        if possible[j]:
            impossible = False
            least = min(num[j],least)
    if impossible:
        return min(num),False
    return least,True
def race(track : str, times : int, i : int):
    '''
    Find the shortest amount of jump to the finished line if possible
    If not possible return length left
    '''
    length = len(track)
    while i < length:
        if track[i] in ["o","^"] and track[i+1] != " ":
            i += 1
            times += 1
        elif track[i] == "O":
            if i+3 >= length:
                return times + 1, True
            return recursive(track,times,i)
        elif track[i] == "|":
            return times,True
        else:
            return length-i-1, False
def main():
    '''Driver Code'''
    bubbles = input()
    num, is_possible = race(bubbles,0,0)
    if is_possible:
        print(f"POSSIBLE\n{num}")
    else:
        print(f"IMPOSSIBLE\n{num}")
if __name__ == "__main__":
    main()
