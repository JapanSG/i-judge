'''283 Normal Train'''
def main():
    '''Driver Code'''
    s1,s2 = [station.strip() for station in input().split(sep = ",")]
    pass_s = []
    pass_s_dct = {}
    while True:
        a = input()
        if a.lower() == "done":
            break
        station = [station.strip() for station in a.split(sep = ",")]
        pass_s.append(float(station[1]))
        if station[0]in pass_s_dct:
            print("Error")
            return
        pass_s_dct[station[0]] = float(station[1])
        if s1 in pass_s_dct and s2 in pass_s_dct:
            break
    if s1 not in pass_s_dct or s2 not in pass_s_dct:
        print("Error")
        return
    print(f"{abs(pass_s_dct[s1]-pass_s_dct[s2]):.2f}")
if __name__ == "__main__":
    main()
