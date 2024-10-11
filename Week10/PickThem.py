'''PickThem'''
import json
def main():
    ''':d'''
    listything = input()
    final = json.loads(listything)
    even = False
    for i in final:
        if not i % 2:
            even = True
            print(i)
    if not even:
        print("Nope")
main()
