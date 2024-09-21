'''100m'''
def main():
    """Driver Code"""
    first_time = float(input())
    gold = 1
    silver = 0
    bronze = 0
    gold_time = first_time
    silver_time = 10000000000000
    bronze_time = 10000000000000
    for i in range(2,9):
        time = float(input())
        if time < gold_time:
            gold_time,silver_time,bronze_time = time,gold_time,silver_time
            gold,silver,bronze = i,gold,silver
        elif time < silver_time:
            silver_time,bronze_time = time,silver_time
            silver,bronze = i,silver
        elif time < bronze_time:
            bronze_time = time
            bronze = i
    print(f"{gold} {silver} {bronze}")
main()
