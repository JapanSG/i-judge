'''ticket_fare'''
def get_fare(station,first,cost,second,second_add,third_add,start,end):
    '''get price'''
    if end > station or start > station or end < 1 or start <1:
        print("Error")
        return
    station_traveled = abs(end-start)
    more_c = station_traveled-first-second
    if more_c < 0:
        more_c = 0
    more_b = station_traveled-more_c-first
    if more_b < 0:
        more_b = 0
    total_cost = cost+more_c*third_add+(more_b)*second_add
    #print(more_c)
    #print(cost)
    print(total_cost)
    return
def main():
    '''Driver Code'''
    station = int(input())
    first = int(input())
    cost = int(input())
    second = int(input())
    second_add = int(input())
    third_add = int(input())
    start = int(input())
    end = int(input())
    get_fare(station,first,cost,second,second_add,third_add,start,end)
#get_fare(100,2,20,3,2,1,1,1)
main()
