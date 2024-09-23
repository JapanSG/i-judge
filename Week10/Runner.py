'''Runner'''
def main():
    '''Driver Code'''
    distance = float(input())
    num = int(input())
    least_time = float('inf')
    winner = -1
    winner_spd = 0
    for i in range(num):
        ability = list(map(int, input().split()))
        speed = ability[0]
        starting_point = ability[1]
        time_taken = (distance-starting_point)/speed
        if time_taken < least_time or (time_taken == least_time and winner_spd < speed):
            least_time = time_taken
            winner_spd = speed
            winner = i+1
    print(winner)
if __name__ == "__main__":
    main()
