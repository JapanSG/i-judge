'''ISBN'''
def main():
    '''Driver Code'''
    dct = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":"X",
        "X":10
        }
    isbn = input()
    isbn = [dct[num] for num in isbn.replace(" ","").replace("-","")]
    total = 0
    mult = 10
    for i in isbn[:-1]:
        total += mult*int(i)
        mult -= 1
    check = (-1*total) % 11
    if check == isbn[-1]:
        print("Yes")
    else:
        print(f"No {dct[str(check)]}")
if __name__ == "__main__":
    main()
