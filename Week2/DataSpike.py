'''DataSpike'''
def find_highest(counter,highest):
    '''Find the highest number 8 times recursively'''
    if counter >= 8:
        return highest
    data = int(input())
    if data > highest:
        return find_highest(counter+1,data)
    return find_highest(counter+1,highest)
def main():
    '''driver code'''
    print(find_highest(0,0))
main()
