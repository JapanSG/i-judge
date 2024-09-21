'''meteorite_skjdf'''
def main():
    '''Driver Code'''
    weight = float(input())
    muti = int(input())
    safe = float(input())
    currweight = weight
    shot = 0
    times = 0
    while currweight >= safe:
        shot += muti**times
        times  += 1
        currweight /= muti
    print(shot)
main()
