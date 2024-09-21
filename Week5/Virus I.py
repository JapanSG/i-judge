"""Virus I"""
def main() :
    """function"""
    virus = str(input())
    a = 0
    for i in virus :
        if i == "o" :
            a += 1
    print(a)
main()
