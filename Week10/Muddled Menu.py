'''Muddled Menu'''
def item_check(menu:list,item:str) -> bool:
    '''append or insert item into menu according to number after hastag'''
    if item == "DONE":
        return False
    if item == "CLOSED":
        menu.clear()
        return False
    if item == "SOMETHING'S WRONG":
        menu.clear()
        return True
    if "Can't do:" in item:
        start = item.find(":")+2
        unwanted = item[start:]
        menu.remove(unwanted)
        return True
    hashtag = item.find("#")
    wanted = item[:hashtag-1]
    insert_at_index = item[hashtag+1:]
    if insert_at_index == "N":
        menu.append(wanted)
        return True
    insert_at_index = int(insert_at_index)-1
    if insert_at_index >= len(menu):
        while insert_at_index > len(menu):
            menu.append("")
        menu.append(wanted)
    else:
        menu.insert(insert_at_index,wanted)
    return True
def main():
    '''Driver Code'''
    menu = []
    while True:
        if not item_check(menu,input()):
            break
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
if __name__ == "__main__":
    main()
