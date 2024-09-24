'''BusStop I'''
def main():
    '''Driver Code'''
    cap = int(input())
    stop_num = int(input())
    pass_arrived = 0
    bus = []
    stops = list(range(stop_num))
    for _ in range(stop_num):
        queue = list(map(int, input().split()))
        stop = queue.pop(0)
        stops[stop-1] = queue
    for stop in range(1,stop_num+1):
        pass_arrived += bus.count(stop)
        for _ in range(bus.count(stop)):
            bus.remove(stop)
        for passenger in stops[stop-1]:
            if len(bus) >= cap:
                break
            if passenger <= stop:
                continue
            bus.append(passenger)
    print(pass_arrived)
if __name__ == "__main__":
    main()
