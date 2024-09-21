"""Runner"""
def main():
    """Driver code"""
    MESSAGE = str(input())
    NUMBER_OF_TIME = int(input())
    counter = 0
    while counter < NUMBER_OF_TIME:
        print(MESSAGE)
        counter += 1
main()
