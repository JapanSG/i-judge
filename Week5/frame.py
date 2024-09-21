"""frame"""
def main() :
    """function"""
    message = str(input())
    for _ in range(len(message)+2) :
        print("*",end="")
    print("")
    print("*" + message + "*")
    for _ in range(len(message)+2) :
        print("*",end="")
main()
