"""largest number"""
def shit(NUM1,NUM2,NUM3):
    highest = ""
    mid = ""
    lowest = ""
    if int(NUM1[0]) > int(NUM3[0]):
        highest = NUM1
        if int(NUM2[0]) > int(NUM3[0]):
            mid = NUM2
            lowest = NUM3
        elif int(NUM2[0]) < int(NUM3[0]):
            mid = NUM3
            lowest = NUM2
        else:
            if len(NUM2) > len(NUM3):
                length = len(NUM3)
                if int(NUM2[0:length]) >= int(NUM3[0:length]):
                    mid = NUM2
                    lowest = NUM3
                else:
                    mid = NUM3
                    lowest = NUM2
            elif len(NUM2) < len(NUM3):
                length = len(NUM2)
                if int(NUM3[0:length]) >= int(NUM2[0:length]):
                    mid = NUM3
                    lowest = NUM2
                else:
                    mid = NUM2
                    lowest = NUM3
            else:
                if int(NUM2) > int(NUM3):
                    mid = NUM2
                    lowest = NUM3
                else:
                    mid = NUM3
                    lowest = NUM2
    elif int(NUM1[0]) < int(NUM3[0]):
        highest = NUM3
        mid = NUM1
        lowest = NUM2
    else:
        if len(NUM1) > len(NUM3):
            length = len(NUM3)
            if int(NUM1[0:length]) >= int(NUM3[0:length]):
                highest = NUM1
                mid = NUM3
                lowest = NUM2
            else:
                highest = NUM3
                mid = NUM1
                lowest = NUM2
        elif len(NUM1) < len(NUM3):
            length = len(NUM1)
            if int(NUM3[0:length]) >= int(NUM1[0:length]):
                highest = NUM3
                mid = NUM1
                lowest = NUM2
            else:
                highest = NUM1
                mid = NUM3
                lowest = NUM2
        else:
            if int(NUM1) > int(NUM3):
                highest = NUM1
                mid = NUM3
                lowest = NUM2
            else:
                highest = NUM3
                mid = NUM1
                lowest = NUM2
    return [highest,mid,lowest]
    
def main():
    """Driver Code"""
    highest = ""
    middle = ""
    lowest = ""
    NUM1 = str(input())
    NUM2 = str(input())
    NUM3 = str(input())
    if int(NUM1[0]) > int(NUM2[0]):
        if int(NUM1[0]) > int(NUM3[0]):
            highest = NUM1
            if int(NUM2[0]) > int(NUM3[0]):
                mid = NUM2
                lowest = NUM3
            elif int(NUM2[0]) < int(NUM3[0]):
                mid = NUM3
                lowest = NUM2
            else:
                if len(NUM2) > len(NUM3):
                    length = len(NUM3)
                    if int(NUM2[0:length]) >= int(NUM3[0:length]):
                        mid = NUM2
                        lowest = NUM3
                    else:
                        mid = NUM3
                        lowest = NUM2
                elif len(NUM2) < len(NUM3):
                    length = len(NUM2)
                    if int(NUM3[0:length]) >= int(NUM2[0:length]):
                        mid = NUM3
                        lowest = NUM2
                    else:
                        mid = NUM2
                        lowest = NUM3
                else:
                    if int(NUM2) > int(NUM3):
                        mid = NUM2
                        lowest = NUM3
                    else:
                        mid = NUM3
                        lowest = NUM2
        elif int(NUM1[0]) < int(NUM3[0]):
            highest = NUM3
            mid = NUM1
            lowest = NUM2
        else:
            if len(NUM1) > len(NUM3):
                length = len(NUM3)
                if int(NUM1[0:length]) >= int(NUM3[0:length]):
                    highest = NUM1
                    mid = NUM3
                    lowest = NUM2
                else:
                    highest = NUM3
                    mid = NUM1
                    lowest = NUM2
            elif len(NUM1) < len(NUM3):
                length = len(NUM1)
                if int(NUM3[0:length]) >= int(NUM1[0:length]):
                    highest = NUM3
                    mid = NUM1
                    lowest = NUM2
                else:
                    highest = NUM1
                    mid = NUM3
                    lowest = NUM2
            else:
                if int(NUM1) > int(NUM3):
                    highest = NUM1
                    mid = NUM3
                    lowest = NUM2
                else:
                    highest = NUM3
                    mid = NUM1
                    lowest = NUM2
    elif int(NUM1[0]) < int(NUM2[0]):
        lis = shit(NUM2,NUM1,NUM3)
main()
