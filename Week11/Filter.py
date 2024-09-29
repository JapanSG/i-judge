'''Filter'''
import json
def main():
    '''Driver Code'''
    jsonstr = input()
    students = json.loads(jsonstr)
    filter_num = float(input())
    over = []
    for id_num in students:
        if students[id_num] >= filter_num:
            over.append(id_num)
    over = sorted(over,key = int)
    for id_num in over:
        print(f"{id_num}	{students[id_num]:.2f}")
    if not over:
        print("Nope")
if __name__ == "__main__":
    main()
