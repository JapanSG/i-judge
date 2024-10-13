'''RectangleArea'''
def main():
    '''Driver Code'''
    atr1 = [int(i) for i in input().split()]
    atr2 = [int(i) for i in input().split()]
    rec1 = {
        "bl" : {'x' : atr1[0],
                'y' : atr1[1]
                },
        "tr" : {'x' : atr1[0]+atr1[2],
                'y' : atr1[1]+atr1[3]
                }
    }
    rec2 = {
        "bl" : {'x' : atr2[0],
                'y' : atr2[1]
                },
        "tr" : {'x' : atr2[0]+atr2[2],
                'y' : atr2[1]+atr2[3]
                }
    }
    bl = (max(rec1["bl"]["x"], rec2["bl"]["x"]), max(rec1["bl"]["y"], rec2["bl"]["y"]))
    tr = (min(rec1["tr"]["x"], rec2["tr"]["x"]), min(rec1["tr"]["y"], rec2["tr"]["y"]))
    if bl[0] > tr[0] or bl[1] > tr[1]:
        print("no overlapping")
    else:
        print((tr[0]-bl[0])*(tr[1]-bl[1]))
if __name__ =="__main__":
    main()
