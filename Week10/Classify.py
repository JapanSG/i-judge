'''Classify'''
def print_stu(stu:dict):
    '''Print stu'''
    years = sorted(list(stu))
    for year in years:
        schools = sorted(list(stu[year]))
        printed = False
        for school in schools:
            if printed:
                print(f"-- {int(school)} {stu[year][school]}")
            else:
                printed = True
                print(f"{year} {int(school)} {stu[year][school]}")

def main():
    '''Driver Code'''
    stu = {}
    while True:
        code = input()
        if code == "END":
            break
        year = code[:2]
        school = code[2:4]
        if year in stu:
            if school in stu[year]:
                stu[year][school] += 1
            elif not stu[year]:
                stu[year] = {}
                stu[year][school] = 1
            else:
                stu[year][school] = 1
        else:
            stu[year] = {}
            stu[year][school] = 1
    print_stu(stu)
if __name__ == "__main__":
    main()
