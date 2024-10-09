'''mean'''
def main():
    '''midterms :sob:'''
    students_num = int(input())
    students_lis = []
    score_lis = []
    for _ in range(students_num):
        pro = input().split()
        students_lis.append(pro[0])
        score_lis.append(pro[1])
    score_lis = list(map(float,score_lis))
    avg = sum(score_lis)/students_num
    closest = -10000000000000000000
    middest_student = ""
    for i in range(students_num):
        if avg - score_lis[i] < avg-closest and score_lis[i] <= avg:
            closest = score_lis[i]
            middest_student = students_lis[i]
    print(f"{middest_student}	{closest}")
main()
