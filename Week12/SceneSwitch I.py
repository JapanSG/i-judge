'''SceneSwitch I'''
#[switch on/off, is_WarmWhite]
def main():
    '''Driver Code'''
    is_on = False
    curr_light = True
    total = 0
    prev_time = 0
    while True:
        time = input()
        if time == "End":
            break
        time = float(time)
        dif = time-prev_time
        if is_on:
            is_on = False
        elif dif <= 6:
            is_on = True
            curr_light = not curr_light
            if curr_light:
                total += 1
        else:
            is_on = True
            curr_light = False
        prev_time = time
    print(total)
if __name__ == "__main__":
    main()
