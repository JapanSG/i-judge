'''Roman'''
def roman_to_int(num:str) -> int:
    '''Convert roman to int'''
    numbers = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    length = len(num)
    val = 0
    i = 0
    while i < length:
        char = num[i]
        if char == "M":
            val += 1000
        elif char == "D":
            val += 500
        elif char =="C":
            if i + 1 < length and num[i+1] in "DM":
                val += numbers[num[i+1]] - 100
                i += 2
                continue
            val += 100
        elif char == "L":
            val += 50
        elif char == "X":
            if i + 1 < length and num[i+1] in "LC":
                val += numbers[num[i+1]] - 10
                i += 2
                continue
            val += 10
        elif char == "V":
            val += 5
        else:
            if i + 1 < length and num[i+1] in "VX":
                val += numbers[num[i+1]] -1
                i += 2
                continue
            val += 1
        i += 1
    return val
def main():
    '''Driver Code'''
    print(roman_to_int(input()))
if __name__ == "__main__":
    main()
