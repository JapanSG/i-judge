"""Grade2"""
def main():
    """Driver"""
    GRADE = float(input())
    if 100 >= GRADE >= 95:
        print("A")
    elif 95 > GRADE >= 90:
        print("B+")
    elif 90 > GRADE >= 85:
        print("B")
    elif 85 > GRADE >= 80:
        print("C+")
    elif 80 > GRADE >= 75:
        print("C")
    elif 75 > GRADE >= 70:
        print("D+")
    elif 70 > GRADE >= 65 :
        print("D")
    elif 65 > GRADE >= 60:
        print("F+")
    elif 60 > GRADE >= 0:
        print("F")
    else:
        print("ERR")
main()
