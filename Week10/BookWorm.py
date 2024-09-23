'''boowor'''
def test(tim_had,boo_num) -> int:
    '''return how many bono can a wor rea'''
    tim = 0
    bono_rea = 0
    bono_tims = []
    for _ in range(boo_num):
        bono_tim = float(input())
        bono_tims.append(bono_tim)
    bono_tims.sort()
    for i in bono_tims:
        if tim + i > tim_had:
            return bono_rea
        tim += i
        bono_rea += 1
    return bono_rea

def main():
    '''Driver Code'''
    wor_num = int(input())
    for _ in range(wor_num):
        tim_had = float(input())
        boo_num = int(input())
        print(test(tim_had,boo_num))

if __name__ == "__main__":
    main()
