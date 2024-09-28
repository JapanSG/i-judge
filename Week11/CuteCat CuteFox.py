'''CuteCat CuteFox'''
import re
def main():
    '''Driver Code'''
    num = int(input())
    re_pattern = r"\"[^\" :]+\""
    re_patter2 = r"\'[^\' :]+\'"
    cat_num = 0
    fox_num = 0
    dct = {}
    for _ in range(num):
        string = input()
        lis = re.findall(re_pattern,string)
        if not lis:
            lis = re.findall(re_patter2,string)
        animal = {lis[0][1:-1]:lis[1][1:-1]}
        dct.update(animal)
    values = list(dct.values())
    keys = dct
    if not ("Cat01" in values or "Garfield" in keys):
        dct.update({"Garfield":"Cat01"})
    if not("Fox01" in values or "Fubuki" in keys):
        dct.update({"Fubuki":"Fox01"})
    for item in dct.items():
        if item[1][:3].lower() == "cat":
            cat_num += 1
        else:
            fox_num += 1
    print(f"Cat : {cat_num}")
    print(f"Fox : {fox_num}")
    sorted_key = sorted(dct,key = lambda x : [dct[x][0].upper(),len(dct[x]),dct[x][3:]])
    for key in sorted_key:
        print(f"{key} : {dct[key]}")
if __name__ == "__main__":
    main()
