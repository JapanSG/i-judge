'''Olympic'''
def to_dict(data:str) -> dict:
    '''Convert String to dict'''
    lis = data.split()
    return {lis[0] : list(map(int, lis[1:]))}
def main():
    '''Driver Code'''
    countries = {}
    country_num = int(input())
    for _ in range(country_num):
        countries.update(to_dict(input()))
    keys = sorted(countries,key = lambda key:(list(map(lambda x : x*-1 ,countries[key])),key),)
    length = len(keys)
    prev_pos = 0
    for pos in range(1,length+1):
        key = keys[pos-1]
        medals = countries[key]
        if prev_pos > 0 and medals == countries[keys[prev_pos-1]]:
            print(f"{prev_pos} {key} {medals[0]} {medals[1]} {medals[2]} {sum(medals)}")
        else:
            print(f"{pos} {key} {medals[0]} {medals[1]} {medals[2]} {sum(medals)}")
            prev_pos = pos
if __name__ == "__main__":
    main()
