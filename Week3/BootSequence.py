'''BootSequence'''
def main():
    '''driver code'''
    most = int(input())+1
    print(1,end = "")
    for i in range(2,most):
        print("_",i, end = "",sep = "")
main()
