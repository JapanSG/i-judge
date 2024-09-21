'''Cat Parade'''
def print_dict(dic:dict):
    '''print dict'''
    lis = sorted(dic.keys())
    for key in lis:
        print(f"{key} {dic[key][0]} {dic[key][1]}")
def main():
    '''Driver Code'''
    cats = {}
    i = 1
    while True:
        line = input().split(", ")
        for species in line:
            if species == "IT'S A DOG":
                cats.popitem()
                i -= 1
            elif species == "END":
                print_dict(cats)
                return
            else:
                if species in cats:
                    cats[species][1] += 1
                    i+=1
                else:
                    cats[species] = [i,1]
                    i+=1
if __name__ == "__main__":
    main()
