'''Grade III'''
import math
def main():
    '''Driver code'''
    num = int(input())
    total = 0.0
    for _ in range(num):
        score = float(input())
        if score >= 95:
            total += 4.0
        elif score >=90:
            total += 3.5
        elif score >= 85:
            total += 3.0
        elif score >=  80:
            total += 2.5
        elif score >= 75:
            total += 2
        elif score >= 70:
            total += 1.5
        elif score >= 65:
            total += 1.0
        elif score >= 60:
            total += 0.5
        else:
            total += 0.0
    print(f"{math.floor(total/num*100)/100:.2f}")
main()
