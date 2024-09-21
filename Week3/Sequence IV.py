"""Sequence IV"""
def main():
    """Sequence IV"""
    x = int(input())
    for i in range(x):
        for j in range(1+(x*i) , x +(x * i)+1):
            print(j , end=" ")
        print("")
main()
