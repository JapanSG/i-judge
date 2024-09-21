'''Counting Stars'''
def main():
    '''Drive Code'''
    sky = input()
    con,com,sho,i = 0,0,0,0
    while i+1 < len(sky):
        star = sky[i:i+2]
        if star == "**":
            con += 1
            i += 2
        elif star in ("~*","*~"):
            com += 1
            i += 2
        elif star == "*/":
            sho += 1
            i += 2 
        else:
            i += 1
    if [con,com,sho]==[0,0,0]:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {con}\ncomet: {com}\nshooting star: {sho}")
main()
