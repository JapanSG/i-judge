"""Kaprekar"""
def arrange(lis):
    '''bubble sor-T'''
    length = len(lis)
    for i in range(0,length):
        for j in range(i,length):
            if lis[i] > lis[j]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
def better_split(string):
    '''convert string to list'''
    lis = []
    for i in string:
        lis.append(i)
    return lis
def main():
    '''driver'''
    x = f"{int(input()):04d}"
    times = 0
    while x != "6174":
        lis = list(map(int,better_split(x)))
        arrange(lis)
        most  = ""
        least = ""
        for i in lis:
            least += str(i)
        most = least[::-1]
        x  = f"{abs(int(most)-int(least)):04d}"
        times +=1
    print(times)
main()
