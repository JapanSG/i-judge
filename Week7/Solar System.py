'''Solar'''
def get_sun_index(solar : str) -> int:
    '''return the location of the sun'''
    index = 0
    string = ""
    for i in solar:
        if string == "Sun" and i.isspace():
            return index
        if i.isspace():
            index += 1
            string = ""
            continue
        string += i
    return index
def get_last_index(solar : str) -> int:
    '''return last index'''
    index = 0
    for i in solar:
        if i.isspace():
            index += 1
    return index
def get_planet(solar : str, planet_index : int) -> str:
    '''return planet based on index'''
    index = 0
    string = ""
    for i in solar:
        if i.isspace() and index == planet_index:
            return string
        if index == planet_index:
            string += i
        if i.isspace():
            index += 1
    return string
def main():
    '''Driver Code'''
    solar = input()
    last = get_last_index(solar)
    sun_index = get_sun_index(solar)
    if sun_index-1 >= 0 and sun_index+1 <= last:
        print(f"Hot: {get_planet(solar,sun_index-1)} {get_planet(solar,sun_index+1)}")
    elif sun_index-1 < 0:
        print(f"Hot: {get_planet(solar,sun_index+1)}")
    elif sun_index+1 > last:
        print(f"Hot: {get_planet(solar,sun_index-1)}")
    if last-sun_index > sun_index-0:
        print(f"Cool: {get_planet(solar,last)}")
    elif sun_index-0 > last-sun_index:
        print(f"Cool: {get_planet(solar,0)}")
    else:
        print(f"Cool: {get_planet(solar,0)} {get_planet(solar,last)}")
main()
