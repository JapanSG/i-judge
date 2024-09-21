"""largest number"""
def main():
    """Driver Code"""
    highest = ""
    middle = ""
    lowest = ""
    NUM1 = str(input())
    NUM2 = str(input())
    NUM3 = str(input())
    FNUM1 = int(NUM1[0])
    FNUM2 = int(NUM2[0])
    FNUM3 = int(NUM3[0])
    if FNUM1 > FNUM2:
        highest = NUM1
        middle = NUM2
    elif FNUM1 < FNUM2:
        highest = NUM2
        middle = NUM1
    else:
        if len(NUM1) == len(NUM2):
            if int(NUM1) > int(NUM2):
                highest = NUM1
                middle = NUM2
            else:
                highest = NUM2
                middle = NUM1
        else:
            if len(NUM1) > len(NUM2):
                if int(NUM1[1]) <= int(NUM2[0]):
                    highest = NUM2
                    middle = NUM1
                else:
                    highest = NUM1
                    middle = NUM2
            else:
                if int(NUM2[1]) <= int(NUM1[0]):
                    highest = NUM1
                    middle = NUM2
                else:
                    highest = NUM2
                    middle = NUM1
    if FNUM3 > int(highest[0]):
        lowest = middle
        middle = highest
        highest = NUM3
    elif FNUM3 < int(highest[0]):
        if FNUM3 > int(middle[0]):
            lowest = middle
            middle = NUM3
        elif FNUM3 < FNUM2:
            lowest = NUM3
        else:
            if int(NUM3) > int(middle):
                lowest = middle
                middle = NUM3
            else:
                lowest = NUM3
    else:
        if int(NUM3) >= int(highest):
            lowest = middle
            middle = highest
            highest = NUM3
        else:
            if FNUM3 > int(middle[0]):
                lowest = middle
                middle = NUM3
            elif FNUM3 < FNUM2:
                lowest = NUM3
            else:
                if int(NUM3) > int(middle):
                    lowest = middle
                    middle = NUM3
                else:
                    lowest = NUM3
    print(int(highest+middle+lowest))
    

main()
