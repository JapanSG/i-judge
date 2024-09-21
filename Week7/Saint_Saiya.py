"""Saint Seiya"""
def rolling_crash(sec:int,left:int)-> int:
    '''Return number of normal punches after ペガサスローリングクラッシュ'''
    normal_punchs = 12*(left-(sec))
    return normal_punchs
def main():
    '''Driver Code'''
    second = int(input())
    punch = int(input())
    total1 = 165*(second//2)-(164*(second//6))
    sets = punch//331
    second_past = sets*6+1
    total2 = (sets)*331
    while second_past <= second and total2 < punch:
        if not second_past%6:
            total2 += 1
        elif not second_past%2:
            total2 += 165
        second_past +=1
    if total1 <= total2:
        print(total1)
    elif total2 < total1:
        print(total2+rolling_crash(second_past,second))
if __name__ == "__main__":
    main()
