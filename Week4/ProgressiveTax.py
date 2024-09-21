'''ProgressiveTax'''
def main():
    '''Driver Code'''
    sal = int(input())
    final = 0
    if sal > 4000000:
        final += (sal-(4000000))*35//100
        sal = 4000000
    if sal > 2000000:
        final += (sal-(2000000))*30//100
        sal = 2000000
    if sal > 1000000:
        final += (sal-(1000000))*25//100
        sal = 1000000
    if sal > 750000:
        final += (sal-(750000))*20//100
        sal = 750000
    if sal > 500000:
        final += (sal-(500000))*15//100
        sal = 500000
    if sal > 300000:
        final += (sal-(300000))*10//100
        sal = 300000
    if sal > 150000:
        final += (sal-(150000))*5//100
        sal = 150000
    print(final)
main()
